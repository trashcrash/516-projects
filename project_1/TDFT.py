import matplotlib.pyplot as pyplot
from scipy import fftpack
import numpy as np
import show_wav
FILENAME = show_wav.FILENAME
WINDOW_WIDTH = 0.02
sound, frame_rate, frame_num, channel_num = show_wav.read_wav(FILENAME)
window_width = int(WINDOW_WIDTH*frame_rate)
if channel_num > 1:
    sound = sound.sum(axis = 1)
def fft_in_window(begin, sound, window_width):
    spectrum_in_window = fftpack.fft(sound[begin:begin+window_width])
    return spectrum_in_window
sound = np.append(sound, np.zeros(window_width))
spectrum = fft_in_window(0, sound, window_width)
for n in range(window_width, frame_num, window_width):
    spectrum_in_window = fft_in_window(n, sound, window_width)
    spectrum = np.vstack((spectrum, spectrum_in_window))
sign_mat = np.sign(spectrum.real)
spectrum = abs(spectrum)*sign_mat