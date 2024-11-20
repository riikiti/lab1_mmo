import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def initialize_plot(root):
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()
    return fig, ax, canvas


def plot_classification(ax, canvas, x, y, metka, a=0, b=0):
    # Очистка предыдущего содержимого графика
    ax.clear()
    # Установка заголовка графика
    ax.set_title("График классификации")

    # Отрисовка точек
    for i in range(len(x)):
        # Если метка точки равна 1, используем красный цвет, иначе — синий
        color = 'red' if metka[i] == 1 else 'blue'
        # Рисуем точку в координатах (x[i], y[i])
        ax.plot(x[i], y[i], 'o', color=color)

    # Установка пределов осей
    ax.set_xlim([0, 100])
    ax.set_ylim([0, 100])

    # Если переданы параметры прямой, добавляем её на график
    if a != 0 or b != 0:
        # Вычисляем координаты концов линии для заданного диапазона x
        x_vals = np.array([0, 100])
        y_vals = a * x_vals + b
        # Рисуем прямую чёрным цветом
        ax.plot(x_vals, y_vals, 'k-')

    # Обновляем canvas, чтобы изменения отображались на экране
    canvas.draw()


def plot_regression(ax, canvas, y, a=0, b=0):
    # Очищаем содержимое осей, чтобы удалить предыдущий график
    ax.clear()

    # Устанавливаем заголовок графика
    ax.set_title("График регрессии")

    # Рисуем точки значений y красными кружками
    # Диапазон x — это индексы элементов массива y
    ax.plot(range(len(y)), y, 'ro')

    # Устанавливаем пределы для оси X (0 до 100)
    ax.set_xlim([0, 100])

    # Устанавливаем пределы для оси Y, немного расширяя диапазон значений y
    ax.set_ylim([min(y) - 1, max(y) + 1])

    # Если переданы параметры прямой регрессии (a и b), строим линию
    if a != 0 or b != 0:
        # Определяем координаты x для линии (от 0 до 100)
        x_vals = np.array([0, 100])
        # Вычисляем соответствующие y для этих x по уравнению y = ax + b
        y_vals = a * x_vals + b
        # Рисуем прямую чёрным цветом
        ax.plot(x_vals, y_vals, 'k-')

    # Обновляем canvas, чтобы изменения стали видимыми
    canvas.draw()
