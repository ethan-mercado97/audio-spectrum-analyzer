import numpy as np
import sounddevice as sd
import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets
from scipy.fft import fft

# ================= SETTINGS =================
SAMPLE_RATE = 44100
CHUNK = 2048
MAX_FREQ = 12000

ALPHA = 0.2

# ================= POSITIVE FREQUENCY AXIS =================
freqs = np.linspace(0, SAMPLE_RATE / 2, CHUNK // 2)

# log frequency axis (must be increasing!)
log_freqs = np.logspace(np.log10(20), np.log10(MAX_FREQ), num=400)

# ================= STATE =================
prev_linear = np.zeros(len(log_freqs))
prev_db = np.zeros(len(log_freqs))
peak_db = np.full(len(log_freqs), -120.0)

# ================= GUI =================
app = QtWidgets.QApplication([])

win = pg.GraphicsLayoutWidget(title="Real-Time Audio Spectrum Analyzer (Fixed Log)")

plot1 = win.addPlot(title="Linear Spectrum (Log Frequency)")
curve1 = plot1.plot()
plot1.setXRange(20, MAX_FREQ)
plot1.setLogMode(x=True)

win.nextRow()

plot2 = win.addPlot(title="dB Spectrum")
curve2 = plot2.plot()
plot2.setXRange(20, MAX_FREQ)
plot2.setYRange(-100, 0)
plot2.setLogMode(x=True)

win.nextRow()

plot3 = win.addPlot(title="Peak Hold (dB)")
curve3 = plot3.plot()
plot3.setXRange(20, MAX_FREQ)
plot3.setYRange(-100, 0)
plot3.setLogMode(x=True)

# ================= AUDIO CALLBACK =================
def audio_callback(indata, frames, time, status):
    global prev_linear, prev_db, peak_db

    audio = indata[:, 0]

    # FFT (positive half only)
    spectrum = np.abs(fft(audio))[:CHUNK // 2]

    # dB
    db = 20 * np.log10(spectrum + 1e-6)

    # IMPORTANT: interpolate ONLY from positive spectrum
    linear_interp = np.interp(log_freqs, freqs, spectrum)
    db_interp = np.interp(log_freqs, freqs, db)

    # smoothing
    linear = ALPHA * linear_interp + (1 - ALPHA) * prev_linear
    db_smooth = ALPHA * db_interp + (1 - ALPHA) * prev_db

    prev_linear = linear
    prev_db = db_smooth

    # peak hold
    peak_db = np.maximum(peak_db, db_smooth)
    peak_db -= 0.2
    peak_db = np.maximum(peak_db, -120)

    # update plots (CRITICAL: matching sizes)
    curve1.setData(log_freqs, linear)
    curve2.setData(log_freqs, db_smooth)
    curve3.setData(log_freqs, peak_db)

# ================= AUDIO STREAM =================
stream = sd.InputStream(
    samplerate=SAMPLE_RATE,
    blocksize=CHUNK,
    channels=1,
    callback=audio_callback,
    latency='low'
)

stream.start()

# ================= RUN =================
win.show()
QtWidgets.QApplication.instance().exec()