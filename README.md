# Real-Time Audio Spectrum Analyzer (FFT-Based DSP System)

## Overview
This project implements a real-time audio spectrum analyzer in Python, designed to visualize and analyze live audio signals using Fast Fourier Transform (FFT). The system performs continuous signal acquisition, spectral analysis, and real-time visualization with logarithmic frequency scaling and dB magnitude representation.

The goal of this project is to explore practical digital signal processing (DSP) concepts in a real-world audio pipeline, similar to tools used in audio engineering, embedded audio systems, and professional sound analysis workflows.

---

## System Architecture

The system follows a real-time DSP pipeline:

Microphone → Audio Interface → Python Audio Buffer → FFT Processing → Spectral Conversion → Visualization

Key processing stages:
- Real-time audio sampling via external USB interface
- Windowed FFT computation for frequency domain conversion
- Magnitude extraction and dB scaling
- Logarithmic frequency mapping for perceptual alignment
- Real-time GUI rendering using PyQtGraph

---

## Features

### Signal Processing
- Real-time Fast Fourier Transform (FFT)
- Magnitude spectrum computation
- dB-scale conversion for perceptual amplitude representation
- Exponential smoothing for stable visualization
- Peak-hold tracking with decay behavior

### Visualization
- Real-time frequency spectrum display
- Logarithmic frequency axis (20 Hz – 12 kHz)
- Dual-domain representation (linear + dB views)
- High-refresh-rate plotting using PyQtGraph

### System Performance
- Low-latency audio buffering
- Continuous real-time streaming
- Stable multi-plot rendering architecture

---

## Hardware Setup

This project uses external audio acquisition hardware to ensure high-quality sampling and reduced latency:

- Focusrite Scarlett 2i2 — Used for analog-to-digital conversion and low-latency audio streaming
- Audio-Technica AT2020 condenser microphone — Used for high-fidelity audio capture

This setup allows analysis of real-world acoustic signals rather than synthetic inputs.

---

## Software Stack

- Python 3.x
- NumPy (numerical computation)
- SciPy (FFT processing)
- SoundDevice (audio streaming)
- PyQtGraph (real-time visualization)
- PyQt6 (GUI backend)

---

## Installation

Clone the repository:

git clone https://github.com/ethan-mercado97/audio-spectrum-analyzer.git  
cd audio-spectrum-analyzer  

Install dependencies:

pip install -r requirements.txt  

Run the application:

python fft.py  

---

## Testing & Validation

The system was evaluated using controlled and real-world audio inputs to verify correctness and stability.

### 1. Frequency Accuracy Test
- Input: Single-tone sine waves (e.g., 440 Hz, 1 kHz)
- Result: Peak detection aligned within expected FFT resolution limits
- Outcome: Verified frequency-domain correctness

### 2. Multi-Tone Resolution Test
- Input: Multiple simultaneous sine waves
- Result: Distinct spectral peaks successfully resolved
- Outcome: Validated FFT bin resolution and separation capability

### 3. Noise Floor Characterization
- Input: Silent room environment (no active signal)
- Result: Stable noise floor observed (~-80 dB to -90 dB range)
- Outcome: Confirmed system stability under low-signal conditions

### 4. Real-Time Stability Test
- Input: Continuous microphone audio (speech and ambient sound)
- Result: Stable operation over extended runtime (>30 minutes)
- Outcome: No buffer underruns or visualization freezing observed

---

## Performance Considerations

- Chunk size tuning used to balance latency vs. frequency resolution
- Exponential smoothing applied to reduce spectral jitter
- Optimized FFT pipeline for real-time visualization constraints
- Log-frequency interpolation used for perceptual alignment

---

## Future Improvements

- GUI controls for gain and input device selection
- Switchable linear/log frequency modes
- Real-time filter bank (octave / 1/3 octave analysis)
- Audio recording and export functionality
- Advanced DSP features (noise gating, EQ visualization)
- Embedded deployment (Raspberry Pi / DSP hardware port)

---

## Engineering Relevance

This project demonstrates core concepts relevant to:
- Digital Signal Processing (DSP)
- Audio systems engineering
- Real-time data visualization
- Embedded audio pipelines
- Hardware-software integration

---

## Author

Ethan Mercado  
Electrical Engineering & Applied Physics, UC Irvine  
Incoming M.S. Electrical Engineering, USC (Fall 2026)