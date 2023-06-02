import wave
from tkinter import Tk, filedialog

import matplotlib.pyplot as plt
import numpy as np


def select_audio_file():
    # Создаем экземпляр Tk
    root = Tk()
    # Скрываем основное окно Tkinter
    root.withdraw()

    # Открываем диалоговое окно для выбора файла
    file_path = filedialog.askopenfilename(filetypes=[("WAV Files", "*.wav")])

    return file_path


def plot_audio_spectrum(filename):
    # Открываем аудиофайл
    with wave.open(filename, 'rb') as wav_file:
        # Получаем параметры аудиофайла
        num_channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        sample_rate = wav_file.getframerate()
        num_frames = wav_file.getnframes()

        # Читаем аудиоданные
        audio_data = wav_file.readframes(num_frames)

    # Преобразуем байтовые данные в массив NumPy
    if sample_width == 2:
        audio_data = np.frombuffer(audio_data, dtype=np.int16)
    elif sample_width == 4:
        audio_data = np.frombuffer(audio_data, dtype=np.int32)

    # Вычисляем время для оси x
    duration = num_frames / sample_rate
    time = np.linspace(0, duration, num=len(audio_data))

    # Создаем график
    plt.figure(figsize=(10, 4))
    plt.plot(time, audio_data)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title('Audio Spectrum')
    plt.grid(True)
    plt.show()


# Выбираем аудиофайл
filename = select_audio_file()

if filename:
    # Показываем амплитудно-частотную характеристику выбранного аудиофайла
    plot_audio_spectrum(filename)
