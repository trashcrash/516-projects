import matplotlib.pyplot as pyplot
from scipy import fftpack
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Import from task 1
import show_wav
FILENAME = show_wav.FILENAME
WINDOW_WIDTH = 0.02
sound, frame_rate, frame_num, channel_num = show_wav.read_wav(FILENAME)

# Translate window width to indices
window_width = int(WINDOW_WIDTH*frame_rate)
if channel_num > 1:
    sound = sound.sum(axis = 1)

# fft to the signal in the window
def fft_in_window(begin, sound, window_width):
    spectrum_in_window = fftpack.fft(sound[begin:begin+window_width])
    return spectrum_in_window

# Calculate dtft, L = window_width, M = window_width
def get_tdft(sound, window_width, frame_num, L):
    sound = np.append(sound, np.zeros(window_width))
    spectrum = fft_in_window(0, sound, window_width)
    for n in range(window_width, frame_num, L):
        spectrum_in_window = fft_in_window(n, sound, window_width)
        spectrum = np.vstack((spectrum, spectrum_in_window))
    return spectrum

if __name__ == '__main__':
    L = window_width
    spectrum = get_tdft(sound, window_width, frame_num, L)
    fig = pyplot.figure()
    ax = fig.gca(projection='3d')
    xs = np.arange(spectrum.shape[0])
    ys = np.arange(spectrum.shape[1])
    xs, ys = np.meshgrid(xs, ys)
    sign_mat = np.sign(spectrum.real)
    spectrum_amplitude = abs(spectrum)*sign_mat
    zs = np.log10(np.transpose(spectrum_amplitude))
    surf = ax.plot_surface(xs, ys, zs, cmap=cm.coolwarm,\
                       linewidth=0, antialiased=False)
    ax.set_xlabel('n')
    ax.set_ylabel('omega')
    ax.set_zlabel('power of 10')
    pyplot.show()