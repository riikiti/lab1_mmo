import random
import tkinter as tk
from tkinter import Label, Button
from classification import classification
from regression import regress
from plotting import plot_classification, plot_regression, initialize_plot


class Lab1App:
    def __init__(self, root):
        self.root = root
        self.root.title("Lab1 Application")

        # Метки и начальные данные
        self.metka_without = [1] * 30
        self.w_res = [0, 0, -1]
        self.y_res = [-0.11, -2.94, 0.26, 2.29, 0.02, 0.51, -0.91, 0.03, 0.29, -0.83,
                      -1.41, -1.28, -0.41, 1.04, -1.27, 0.89, 0, -0.48, 0.28, -0.08,
                      0.45, 0.47, -1.47, 0.45, -1.3, 0.93, 0.6, 1.06, 0.6, -0.93,
                      -0.53, -0.69, -2.42, -0.76, -0.84, 0.29, -0.35, 1.82, -1.52, 0.27,
                      1.38, 1.1, -0.22, -0.79, -0.91, 0.14, -0.32, -1.19, -0.28, -0.84]

        # GUI Elements
        self.label1 = Label(root, text="Уравнение не найдено")
        self.label1.pack()
        self.label2 = Label(root, text="")
        self.label2.pack()

        self.button1 = Button(root, text="Запустить классификацию", command=self.run_classification)
        self.button1.pack()

        self.button2 = Button(root, text="Запустить регрессию", command=self.run_regression)
        self.button2.pack()

        # Graphs
        self.fig, self.ax, self.canvas = initialize_plot(self.root)

    def run_classification(self):
        # Генерация случайных координат точек x, y в диапазоне [1, 100]
        x = [random.randint(1, 100) for _ in range(30)]
        y = [random.randint(1, 100) for _ in range(30)]
        # Генерация случайных меток классов для точек: 1 или -1
        metka = [random.choice([1, -1]) for _ in range(30)]
        # Получаем точки, метки и (возможно) их предыдущее распределение через random_liner_yes
        result = self.random_liner_yes(30)
        # Запускаем обучение линейного классификатора
        w = classification(result[0], result[1], result[2])

        # Если обучение не удалось (вес w[2] равен 0), сообщаем, что разделяющая линия не найдена
        if w[2] == 0:
            self.label1.config(text="Уравнение не найдено")
            # Рисуем график точек без разделяющей линии
            plot_classification(self.ax, self.canvas, result[0], result[1], result[2])
        else:
            # Вычисляем коэффициенты уравнения прямой: y = a * x + b
            a, b = -w[1] / w[2], -w[0] / w[2]
            # Формируем текст уравнения прямой
            equation_text = f"Уравнение: {a:.2f}x + {b:.2f}"
            # Выводим уравнение на экран
            self.label1.config(text=equation_text)
            # Рисуем график точек с разделяющей прямой
            plot_classification(self.ax, self.canvas, result[0], result[1], result[2], a, b)

    def run_regression(self):
        # Генерация массива случайных значений y (от 0 до 10)
        y = [random.random() * 2.5 for _ in range(50)]
        # Выполнение линейной регрессии. Функция regress возвращает массив весов w:
        # w[0] — свободный член, w[1] — наклон линии, w[2] — индикатор успешности регрессии
        w = regress(y)

        # Проверка, удалось ли построить уравнение прямой
        if w[2] == 0:
            # Если построить уравнение не удалось, отображаем соответствующее сообщение
            self.label2.config(text="Уравнение не найдено")
        else:
            # Формируем текст уравнения в виде "w[1]x + w[0]"
            equation_text = f"Уравнение: {w[1]:.2f}x + {w[0]:.2f}"
            # Выводим уравнение в метке интерфейса
            self.label2.config(text=equation_text)
            # Строим график данных с линией регрессии
            plot_regression(self.ax, self.canvas, y, w[1], w[0])

    def random_liner_yes(self, number):
        # Инициализация результата: три списка для x, y и меток классов
        result = [[], [], []]
        # Случайные параметры прямой: наклон a (отрицательный) и смещение b
        a, b = -random.random(), random.randint(50, 80)

        # Генерация указанного количества точек (number)
        for i in range(number):
            # Случайные координаты точки (x, y_val) в диапазоне [1, 100]
            x, y_val = random.randint(1, 100), random.randint(1, 100)

            # Проверяем, находится ли точка в узкой полосе шириной 8 вокруг прямой
            # Если точка попадает в полосу, пропускаем её
            if (y_val + 4 > x * a + b) and (y_val - 4 < x * a + b):
                continue

            # Добавляем координаты точки в результат
            result[0].append(x)
            result[1].append(y_val)
            # Присваиваем метку классу: 1, если точка выше прямой, -1 — ниже
            result[2].append(1 if y_val > x * a + b else -1)

        # Возвращаем массив с координатами точек и их метками
        return result


# Запуск интерфейса
root = tk.Tk()
app = Lab1App(root)
root.mainloop()
