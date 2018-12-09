from show_wav import read_wav
from scipy import fftpack
import matplotlib.pyplot as pyplot
import numpy as np

DEBUG = True

def pick_window(signal, head, frame_rate, length_sec = 0.02):
    length_n = int(length_sec*frame_rate)
    signal_in_window = signal[head:head+length_n]
    return signal_in_window


def get_channel(signal, channel_num):
    if channel_num > 1:
        channel = signal[:, 0]
    else:
        channel = signal
    return channel


def draw_signal(signal, frame_rate):
    # Normalization
    x = 1/frame_rate*np.arange(signal.size)

    # Show the waveform
    pyplot.plot(x, signal)
    pyplot.title('Hello world!', fontsize = 18)
    pyplot.xlabel('time (seconds)', fontsize = 14)
    pyplot.ylabel('Amplitude (max = 1)', fontsize = 14)
    print('Close plot to terminate')
    pyplot.show()


def draw_dft(magnitude):
    k = np.arange(window.size)
    pyplot.plot(np.log10(magnitude))
    pyplot.title('Hello world!', fontsize = 18)
    pyplot.xlabel('Frequency number (k)', fontsize = 14)
    pyplot.ylabel('Amplitude, power of 10', fontsize = 14)
    print('Close plot to terminate')
    pyplot.show()


def get_autocorr(signal, lag):
    "lag >= 0"
    autocorr = 0
    for i in range(len(signal)-lag):
        autocorr += signal[i+lag]*signal[i]
    return autocorr


def get_autocorr_array(signal, order, k):
    autocorr_array = np.array([])
    for m in range(1, order+1):
        autocorr_array = np.append(autocorr_array, get_autocorr(signal, abs(m-k)))
    return autocorr_array


def get_autocorr_matrix(signal, order):
    autocorr_matrix = get_autocorr_array(signal, order, 1)
    for k in range(2, order+1):
        autocorr_matrix = np.vstack((autocorr_matrix, get_autocorr_array(signal, order, k)))
    return autocorr_matrix


def get_G_square(signal, order, x):
    G_square = np.array(get_autocorr(signal, 0))
    for k in range(1, order+1):
        G_square += get_autocorr(signal, k)*x[k-1]
    return G_square


def get_H(length, x, G):
    denominator = 1
    H = np.array([])
    for k in range(length):
        for i in range(len(x)):
            denominator += x[i]*np.exp(-1j*k/length*(i+1))
        H_k = G/denominator
        H = np.append(H, H_k)
    return H

if __name__ == "__main__":
    order = int(float(input("Please enter the order of the model: ")))
    sound, frame_rate, frame_num, channel_num = read_wav("./helloworld.wav")
    channel = get_channel(sound, channel_num)
    window = pick_window(channel, 40000, frame_rate)/32768
    # window = window*0+1
    window_dft = fftpack.fft(window)
    magnitude = abs(window_dft)
    draw_dft(magnitude)
    # Ax = y
    A = get_autocorr_matrix(window, order)
    y = -1*get_autocorr_array(window, order, 0)
    x = np.linalg.solve(A, y)
    G_square = get_G_square(window, order, x)
    H = get_H(len(window), x, G_square**(0.5))
    magnitude_H = abs(H)
    draw_dft(magnitude_H)
    h = fftpack.ifft(H)
    draw_signal(window, frame_rate)
    draw_signal(abs(h), frame_rate)
    if DEBUG:
        window = np.array([0.5, 1, 2, 1, 0.5, 0.25, 0.125])
        A = get_autocorr_matrix(window, 2)
        y = -1*get_autocorr_array(window, 2, 0)
        x = np.linalg.solve(A, y)
        G_square = get_G_square(window, 2, x)
        print(x)
        print(G_square**0.5)