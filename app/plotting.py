import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def initialize_plot(root):
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()
    return fig, ax, canvas


def plot_classification(ax, canvas, x, y, metka, a=0, b=0):
    ax.clear()
    ax.set_title("График классификации")
    for i in range(len(x)):
        color = 'red' if metka[i] == 1 else 'blue'
        ax.plot(x[i], y[i], 'o', color=color)
    ax.set_xlim([0, 100])
    ax.set_ylim([0, 100])
    if a != 0 or b != 0:
        x_vals = np.array([0, 100])
        y_vals = a * x_vals + b
        ax.plot(x_vals, y_vals, 'k-')
    canvas.draw()


def plot_regression(ax, canvas, y, a=0, b=0):
    ax.clear()
    ax.set_title("График регрессии")
    ax.plot(range(len(y)), y, 'ro')
    ax.set_xlim([0, 100])
    ax.set_ylim([min(y) - 1, max(y) + 1])
    if a != 0 or b != 0:
        x_vals = np.array([0, 100])
        y_vals = a * x_vals + b
        ax.plot(x_vals, y_vals, 'k-')
    canvas.draw()
