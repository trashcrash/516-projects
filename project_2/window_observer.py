from show_wav import read_wav
from scipy import fftpack
import matplotlib.pyplot as pyplot
import numpy as np

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


if __name__ == "__main__":
    sound, frame_rate, frame_num, channel_num = read_wav("./helloworld.wav")
    channel = get_channel(sound, channel_num)
    window = pick_window(channel, 40000, frame_rate)
    window_dft = fftpack.fft(window)
    magnitude = abs(window_dft)
    # Normalization
    x = 1/frame_rate*np.arange(window.size)
    k = np.arange(window.size)

    # Show the waveform
    pyplot.plot(x, window/32768)
    pyplot.title('Hello world!', fontsize = 18)
    pyplot.xlabel('time (seconds)', fontsize = 14)
    pyplot.ylabel('Amplitude (max = 1)', fontsize = 14)
    print('Close plot to terminate')
    pyplot.show()


    pyplot.plot(np.log10(magnitude))
    pyplot.title('Hello world!', fontsize = 18)
    pyplot.xlabel('Frequency number (k)', fontsize = 14)
    pyplot.ylabel('Amplitude (max = 1)', fontsize = 14)
    print('Close plot to terminate')
    pyplot.show()