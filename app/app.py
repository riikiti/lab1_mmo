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
        x = [random.randint(1, 100) for _ in range(30)]
        y = [random.randint(1, 100) for _ in range(30)]
        metka = [random.choice([1, -1]) for _ in range(30)]
        result = self.random_liner_yes(30)
        w = classification(result[0], result[1], result[2])

        if w[2] == 0:
            self.label1.config(text="Уравнение не найдено")
            plot_classification(self.ax, self.canvas, result[0], result[1], result[2])
        else:
            a, b = -w[1] / w[2], -w[0] / w[2]
            equation_text = f"Уравнение: {a:.2f}x + {b:.2f}"
            self.label1.config(text=equation_text)
            plot_classification(self.ax, self.canvas, result[0], result[1], result[2], a, b)

    def run_regression(self):
        y = [random.random() * 10 for _ in range(50)]
        w = regress(y)

        if w[2] == 0:
            self.label2.config(text="Уравнение не найдено")
        else:
            equation_text = f"Уравнение: {w[1]:.2f}x + {w[0]:.2f}"
            self.label2.config(text=equation_text)
            plot_regression(self.ax, self.canvas, y, w[1], w[0])

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


# Запуск интерфейса
root = tk.Tk()
app = Lab1App(root)
root.mainloop()
