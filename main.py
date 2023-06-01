import numpy as np
from matplotlib import pyplot as plt
from scipy import signal
from scipy.io import wavfile

if __name__ == '__main__':
    file_name = input("Type file name:\n")
    rate, data = wavfile.read(file_name)
    print(f"Number of channels = {data}")

    x = signal.decimate(data, 4)
    # x = x[48000 * 3:48000 * 3 + 8192]
    x *= np.hamming(x.size)

    x_fft = abs(np.fft.rfft(x))
    x_db = 20 * np.log10(x_fft)
    frequency = np.fft.rfftfreq(x.size, 1 / 48000)

    plt.plot(frequency, x_db)
    plt.show()
