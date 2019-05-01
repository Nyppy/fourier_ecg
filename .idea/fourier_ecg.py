from matplotlib import pyplot as plt
import math

class Ecg_fourier():
    '''Класс производит прямое/обратное преобразование Фурье с ЭКГ'''

    def __init__(self):
        self.ecg_array = list() # полученный масив ЭКГ
        self.input_ecg_up_data = list() # выходной массив прямого преобразования Фурье
        self.input_ecg_down_data = list() # выходной массив обратного преобразования Фурье

    def add_ecg_array(self, add_ecg_array):
        '''Получение данных ЭКГ, через ввод массива'''

        self.ecg_array = add_ecg_array # Массив с полученным  ЭКГ

    def add_ecg_file(self, add_ecg_file):
        '''Получение данных ЭКГ, чтение файла'''

        ecg_array_file = list()
        ecg_tmp = list()
        i = True

        with open(add_ecg_file, 'r') as file:

            while i:
                f = file.readline().strip()
                if f != '':
                    ecg_tmp.append(f.split(' '))
                else:
                    i+=False
                    break

            for i in ecg_tmp:
                for j in i:
                    ecg_array_file.append(int(j))

        self.ecg_array = ecg_array_file # Массив с ЭКГ

    def fourier_up(self):
        '''Прямое преобразование Фурье'''

        N = 128-1
        Pi = math.pi
        # a_k - элементы массива
        k = 1
        S = 1
        file = open('/Users/aroslavbaklanov/Desktop/ecg_fourier_up.txt','w') # создаем файл ecg_fourier_up.txt на рабочем столе, если он уже создан перезаписываем

        for a_k in range(len(self.ecg_array)):
            a_s = ((1/math.sqrt(N) * self.ecg_array[a_k]) * (math.e * (-a_k) * 2 * Pi) * ((k * S)/N))
            self.input_ecg_up_data.append(a_s)
            file.write(str(a_s) + '\n')

        file.close() # закрытие файла

    def fourier_down(self, file_array_ecg):
        '''Обратное преобразование Фурье'''

        N = 128
        Pi = math.pi
        # a_k - элементы массива
        k = 1
        S = 1

        ecg_file_inut = list()
        ecg_tmp = list()
        i = True

        with open(file_array_ecg, 'r') as file_ecg:

            while i:
                f = file_ecg.readline().strip()
                if f != '':
                    ecg_tmp.append(f.split(' '))
                else:
                    i += False
                    break

            for i in ecg_tmp:
                for j in i:
                    ecg_file_inut.append(float(j))

        file = open('/Users/aroslavbaklanov/Desktop/ecg_fourier_down.txt', 'w') # создаем файл ecg_fourier_up.txt на рабочем столе, если он уже создан перезаписываем

        for a_s in range(len(ecg_file_inut)):
            a_k = ((1/math.sqrt(N) * self.ecg_array[a_s]) * (math.e * (-a_s) * 2 * Pi) * ((k * S)/N))
            self.input_ecg_down_data.append(a_k)
            file.write(str(a_k) + '\n')

        file.close() # закрытие файла

    def get_ecg_up_array(self):
        '''Вывод результата прямого преобразования Фурье'''

        len_ecg_array = len(self.ecg_array) # Длина массива ЭКГ
        arr_len_ecg = [i for i in range(1, len_ecg_array+1)] # Массив x координаты ЭКГ

        plt.plot(arr_len_ecg, self.input_ecg_up_data) # Создание графика
        plt.grid(True) # отображение сетки
        plt.show() # Отображение графика

    def get_ecg_down_array(self):
        '''Вывод результата обратного преобразования Фурье'''

        len_ecg_array = len(self.input_ecg_down_data) # Длина массива ЭКГ
        arr_len_ecg = [i for i in range(1, len_ecg_array+1)] # Массив x координаты ЭКГ

        plt.plot(arr_len_ecg, self.input_ecg_down_data) # Создание графика
        plt.grid(True) # отображение сетки
        plt.show() # Отображение графика


arr = [] # предпологаемая переменная с массивом данных ЭКГ


ecg_fourier = Ecg_fourier()  # Экземпляр класса "Ecg_fourier"

# ecg_fourier.add_ecg_array(arr)  # Вызов метода ввода массива ЭКГ, через добовление переменной

ecg_fourier.add_ecg_file('/Users/aroslavbaklanov/PycharmProjects/new_test_python/.idea/text.txt')  # Вызов метода ввода массива ЭКГ, через загрузку файла

ecg_fourier.fourier_up() # метод выполняющий прямое преобразование Фурье
# ecg_fourier.fourier_down('/Users/aroslavbaklanov/Desktop/ecg_fourier_up.txt') # метод обратного преобазования Фурье

ecg_fourier.get_ecg_up_array()  # Вызов метода отображния графика, результат прямого преобразования Фурье
# ecg_fourier.get_ecg_down_array()  # Вызов метода отображния графика, результат обратного преобразования Фурье

