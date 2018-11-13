import TDFT
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as pyplot
import scipy.io.wavfile as wavfile
FILENAME = TDFT.FILENAME
sound, frame_rate = TDFT.sound, TDFT.frame_rate
frame_num, channel_num = TDFT.frame_num, TDFT.channel_num
window_width = TDFT.window_width
L = window_width
spectrum = TDFT.get_tdft(sound, window_width, frame_num, L)
def get_gfbs(spectrum, window_width):
    sound = np.array([])
    for i in range(spectrum.shape[0]):
        sound_in_window = fftpack.ifft(spectrum[i,:])
        sound = np.append(sound, sound_in_window)
    return sound.real
if __name__ == '__main__':
    sound = get_gfbs(spectrum, window_width)
    x = 1/frame_rate*np.arange(sound.size)
    pyplot.plot(x, sound/32768)
    pyplot.title('Hello world!', fontsize = 18)
    pyplot.xlabel('time (seconds)', fontsize = 14)
    pyplot.ylabel('Amplitude (max = 1)', fontsize = 14)
    print('Close plot to terminate')
    pyplot.show()
    wavfile.write("GFBS_helloworld.wav", frame_rate, sound)