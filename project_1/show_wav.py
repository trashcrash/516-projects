import matplotlib.pyplot as pyplot
import scipy.io.wavfile as wavfile
import numpy as np
def read_wav(filename):
    frame_rate, sound = wavfile.read(filename)
    if sound.ndim > 1:
        frame_num, channel_num = sound.shape
    else:
        channel_num = 1
        frame_num = sound.shape[0]
    return sound, frame_rate, frame_num, channel_num
FILENAME = "./helloworld.wav"
if __name__ == '__main__':
    sound, frame_rate, frame_num, channel_num = read_wav(FILENAME)
    if channel_num > 1:
        sound = sound.sum(axis = 1)
    x = 1/frame_rate*np.arange(sound.size)
    pyplot.plot(x, sound/32768)
    pyplot.title('Hello world!', fontsize = 18)
    pyplot.xlabel('time (seconds)', fontsize = 14)
    pyplot.ylabel('Amplitude (max = 1)', fontsize = 14)
    print('Close plot to terminate')
    pyplot.show()