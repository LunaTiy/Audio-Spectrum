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
    chunk_size = 1024  # Размер блока данных для построения графика

    # Открываем аудиофайл
    with wave.open(filename, 'rb') as wav_file:
        # Получаем параметры аудиофайла
        num_channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        sample_rate = wav_file.getframerate()
        num_frames = wav_file.getnframes()

        # Вычисляем длительность и количество блоков данных
        duration = num_frames / sample_rate
        num_blocks = int(num_frames / chunk_size)

        # Создаем график
        plt.figure(figsize=(10, 4))
        plt.xlabel('Time [s]')
        plt.ylabel('Amplitude')
        plt.title('Audio Spectrum')
        plt.grid(True)

        # Читаем и поэтапно строим график для каждого блока данных
        for block_index in range(num_blocks):
            # Читаем блок данных
            audio_data = wav_file.readframes(chunk_size)

            # Преобразуем байтовые данные в массив NumPy
            if sample_width == 2:
                audio_data = np.frombuffer(audio_data, dtype=np.int16)
            elif sample_width == 4:
                audio_data = np.frombuffer(audio_data, dtype=np.int32)

            # Вычисляем время для оси x
            time = np.linspace(
                block_index * chunk_size / sample_rate,
                (block_index + 1) * chunk_size / sample_rate,
                num=len(audio_data)
            )

            # Построение графика
            plt.plot(time, audio_data, color='blue')

        plt.show()


# Выбираем аудиофайл
filename = select_audio_file()
if filename:
    # Показываем амплитудно-частотную характеристику выбранного аудиофайла
    plot_audio_spectrum(filename)
