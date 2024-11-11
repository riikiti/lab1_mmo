import numpy as np
import random
import tkinter as tk
from tkinter import Label, Button
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class Lab1App:
    def __init__(self, root):
        self.root = root
        self.root.title("Lab1 Application")

        # Метки и начальные данные
        self.metka_without = [1] * 30
        self.w_res = [0, 0, -1]
        self.y_res = [
            -0.11, -2.94, 0.26, 2.29, 0.02, 0.51, -0.91, 0.03, 0.29, -0.83,
            -1.41, -1.28, -0.41, 1.04, -1.27, 0.89, 0, -0.48, 0.28, -0.08,
            0.45, 0.47, -1.47, 0.45, -1.3, 0.93, 0.6, 1.06, 0.6, -0.93,
            -0.53, -0.69, -2.42, -0.76, -0.84, 0.29, -0.35, 1.82, -1.52, 0.27,
            1.38, 1.1, -0.22, -0.79, -0.91, 0.14, -0.32, -1.19, -0.28, -0.84
        ]

        # GUI Elements
        self.label1 = Label(root, text="Уравнение не найдено")
        self.label1.pack()
        self.label2 = Label(root, text="")
        self.label2.pack()

        self.button1 = Button(root, text="Run Classification", command=self.run_classification)
        self.button1.pack()

        self.button2 = Button(root, text="Run Regression", command=self.run_regression)
        self.button2.pack()

        # Graphs
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack()

    def classification(self, x, y, metka):
        eta = 0.1
        w = [0, 0, 0]
        metka = [1 if m == 1 else -1 for m in metka]

        for j in range(10000):
            count = 0
            for i in range(len(x)):
                otvet = w[1] * x[i] + w[2] * y[i] + w[0]
                met_otvet = 1 if otvet > 0 else -1
                if met_otvet != metka[i]:
                    delta = metka[i] - met_otvet
                    w[0] += eta * delta
                    w[1] += eta * delta * x[i]
                    w[2] += eta * delta * y[i]
                    count += 1
            if count == 0:
                return w
        w[2] = 0
        return w

    def regress(self, y):
        w = [0, 0, 0]
        result = [0, 0, 0]
        eta = 0.001
        sum_do, sum_do_do = 0, 100000

        for j in range(100000):
            sum_posle = 0
            for i in range(len(y)):
                delta = y[i] - (w[1] * i + w[0])
                d = 1 if delta > 0 else -1
                w[0] += eta * d
                w[1] += eta * d * i
                sum_posle += delta ** 2

            w[2] += 1
            if sum_do == sum_posle and sum_do_do > sum_posle:
                sum_do_do = sum_do
                result = w[:]
            sum_do = sum_posle

        print("Sum Do Do:", sum_do_do)
        return result

    def paint(self, x, y, metka, a=0, b=0):
        self.ax.clear()
        self.ax.set_title("Classification")
        for i in range(len(x)):
            color = 'red' if metka[i] == 1 else 'blue'
            self.ax.plot(x[i], y[i], 'o', color=color)

        x_vals = np.array([0, 100])
        y_vals = a * x_vals + b
        self.ax.plot(x_vals, y_vals, 'k-')
        self.canvas.draw()

    def paint_regress(self, y, a=0, b=0):
        self.ax.clear()
        self.ax.set_title("Regression")
        self.ax.plot(range(len(y)), y, 'ro')

        x_vals = np.array([0, 100])
        y_vals = a * x_vals + b
        self.ax.plot(x_vals, y_vals, 'k-')
        self.canvas.draw()

    def random_liner_yes(self, number):
        result = [[], [], []]
        a, b = -random.random(), random.randint(50, 80)

        for i in range(number):
            x, y_val = random.randint(1, 100), random.randint(1, 100)
            if (y_val + 4 > x * a + b) and (y_val - 4 < x * a + b):
                continue
            result[0].append(x)
            result[1].append(y_val)
            result[2].append(1 if y_val > x * a + b else -1)
        return result

    def run_classification(self):
        x = [random.randint(1, 100) for _ in range(30)]
        y = [random.randint(1, 100) for _ in range(30)]
        metka = [random.choice([1, -1]) for _ in range(30)]
        result = self.random_liner_yes(30)
        w = self.classification(result[0], result[1], result[2])

        if w[2] == 0:
            self.label1.config(text="Уравнение не найдено")
            self.paint(result[0], result[1], result[2])
        else:
            a, b = -w[1] / w[2], -w[0] / w[2]
            equation_text = f"Уравнение: {a:.2f}x + {b:.2f}"
            self.label1.config(text=equation_text)
            self.paint(result[0], result[1], result[2], a, b)

    def run_regression(self):
        y = [random.random() * 10 for _ in range(50)]
        w = self.regress(y)

        if w[2] == 0:
            self.label2.config(text="Уравнение не найдено")
        else:
            equation_text = f"Уравнение: {w[1]:.2f}x + {w[0]:.2f}"
            self.label2.config(text=equation_text)
            self.paint_regress(y, w[1], w[0])


# Запуск интерфейса
root = tk.Tk()
app = Lab1App(root)
root.mainloop()