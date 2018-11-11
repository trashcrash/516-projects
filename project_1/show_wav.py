import matplotlib.pyplot as pyplot
import scipy.io.wavfile as wavfile
import numpy as np

# Read wav file and return the properties
def read_wav(filename):
    frame_rate, sound = wavfile.read(filename)
    if sound.ndim > 1:
        frame_num, channel_num = sound.shape
    else:
        channel_num = 1
        frame_num = sound.shape[0]
    return sound, frame_rate, frame_num, channel_num

# Declare the file name
FILENAME = "./helloworld.wav"
if __name__ == '__main__':

    # Get the properties
    sound, frame_rate, frame_num, channel_num = read_wav(FILENAME)

    # Some wav files have 2 or more channels
    if channel_num > 1:
        sound = sound.sum(axis = 1)

    # Normalization
    x = 1/frame_rate*np.arange(sound.size)

    # Show the waveform
    pyplot.plot(x, sound/32768)
    pyplot.title('Hello world!', fontsize = 18)
    pyplot.xlabel('time (seconds)', fontsize = 14)
    pyplot.ylabel('Amplitude (max = 1)', fontsize = 14)
    print('Close plot to terminate')
    pyplot.show()