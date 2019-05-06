# библиотека matplotlip служит для отображения графиков
from matplotlib import pyplot as plt # из библиотеки импортируем модуль pyplot который называем plt
# библиотека numpy служит для работы с многомерыми массивами (матрицами)
import numpy as np # импортируем библиотеку и называем np
from numpy import fft # импортирем модуль fft, который отвечает за преобразование Фурье

class Ecg_fourier():
    '''Класс производит прямое/обратное преобразование Фурье с ЭКГ'''

    def __init__(self):
        # глобальные переменные
        self.ecg_array = list() # полученный масив ЭКГ
        self.ecg_array_up = list() # массив данных прямого преобразования
        self.rfffft = list() # выходной массив прямого преобразования Фурье
        self.ifffft = list() # выходной массив обратного преобразования Фурье

    def add_ecg_file(self, add_ecg_file):
        '''Получение данных ЭКГ, чтение файла'''

        ecg_array_file = list() # получкнный массив ЭКГ
        ecg_tmp = list() # временная переменная служит для хранения некоторых частей массива ЭКГ
        i = True

        # чтение данных ЭКГ из файла
        with open(add_ecg_file, 'r') as file:
            while i:
                f = file.readline().strip()
                if f != '':
                    ecg_tmp.append(f.split(' '))
                else:
                    i+=False
                    break
            for i in ecg_tmp:
                for j in i: ecg_array_file.append(float(j))

        # записываем полученный массив в глобальную переменную
        self.ecg_array = ecg_array_file # Массив с ЭКГ

    def fourier_up(self):
        '''Прямое преобразование Фурье'''

        # импортируем из бибилиотеки fft метод rfft который совершает прямое преобразование Фурье
        rfffft_temp = fft.rfft(self.ecg_array, n=len(self.ecg_array), axis=-1)

        # записываем полученный массив в глобальную переменную
        self.rfffft = rfffft_temp

    def fourier_down(self):
        '''Обратное преобразование Фурье'''

        # импортируем из бибилиотеки fft метод ifft который совершает обратное преобразование Фурье
        ifffft_temp = fft.ifft(self.rfffft, n=len(self.ecg_array), axis=-1)

        # записываем полученный массив в глобальную переменную
        self.ifffft = ifffft_temp

    def get_ecg_up_array(self):
        '''Вывод результата прямого преобразования Фурье'''

        plt.plot(np.arange(len(self.rfffft)), self.rfffft) # создание графика
        plt.grid(True)  # создание сетки
        plt.show() # отображение графикаё

    def get_ecg_down_array(self):
        '''Вывод результата обратного преобразования Фурье'''

        plt.plot(np.arange(len(self.ecg_array)), self.ifffft) # создание графика
        plt.grid(True) # создание сетки
        plt.show() # отображение графика


ecg_fourier = Ecg_fourier()  # Экземпляр класса "Ecg_fourier"

ecg_fourier.add_ecg_file('/Users/aroslavbaklanov/PycharmProjects/new_test_python/.idea/text.txt')  # Вызов метода ввода массива ЭКГ, через загрузку файла

ecg_fourier.fourier_up() # метод выполняющий прямое преобразование Фурье
ecg_fourier.fourier_down() # метод обратного преобазования Фурье

ecg_fourier.get_ecg_up_array()  # Вызов метода отображния графика, результат прямого преобразования Фурье
# ecg_fourier.get_ecg_down_array()  # Вызов метода отображния графика, результат обратного преобразования Фурье
