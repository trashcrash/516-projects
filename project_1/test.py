import show_wav
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as pyplot
import scipy.io.wavfile as wavfile
FILENAME = show_wav.FILENAME
sound, frame_rate, frame_num, channel_num = show_wav.read_wav(FILENAME)
wavfile.write("test_helloworld.wav", frame_rate, sound)