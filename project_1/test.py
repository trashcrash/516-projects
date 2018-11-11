from scipy import fftpack
import numpy as np
x = np.array([1,2,4,15,15,3,5,6])
print(fftpack.fft(x))