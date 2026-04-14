# Real-Time Audio Spectrum Analyzer

## Overview
This project implements a real-time audio spectrum analyzer using Python. It performs FFT-based signal processing on live microphone input and visualizes the frequency spectrum in both linear and dB scales.

## Features
- Real-time FFT processing
- Logarithmic frequency axis (20 Hz – 12 kHz)
- dB magnitude scaling
- Peak hold tracking
- Multi-plot visualization

## Hardware
- Focusrite Scarlett 2i2
- Audio-Technica AT2020

## How to Run
pip install -r requirements.txt
python fft.py