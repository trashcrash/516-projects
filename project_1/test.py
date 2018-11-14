import show_wav
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as pyplot
import scipy.io.wavfile as wavfile
FILENAME = show_wav.FILENAME
sound, frame_rate, frame_num, channel_num = show_wav.read_wav(FILENAME)
print(type(sound))
finalsound = np.zeros((frame_num, 2))
finalsound[:, 0] = fftpack.ifft(fftpack.fft(sound[:, 0]))
finalsound[:, 1] = fftpack.ifft(fftpack.fft(sound[:, 1]))
finalsound = np.int16((np.round(finalsound.real)))
wavfile.write("test_helloworld.wav", frame_rate, finalsound)