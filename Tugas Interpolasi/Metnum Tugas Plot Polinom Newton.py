import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

def divided_difference(x, y):
    n = len(x)
    coef = y.copy()

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])

    return coef

def newton_interpolation(x, coef, xi):
    n = len(x)
    result = coef[n - 1]

    for i in range(n - 2, -1, -1):
        result = result * (xi - x[i]) + coef[i]

    return result

def plot_interpolation():
    x_values = np.linspace(5, 40, 500)
    y_values = [newton_interpolation(x, coef, xi) for xi in x_values]

    plt.scatter(x, y, color='red', label='Data Points')
    plt.plot(x_values, y_values, label='Newton Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Newton Interpolation')
    plt.legend()
    plt.grid(True)
    plt.show()

# Data contoh
x = [5, 10, 15, 20, 25, 30, 35, 40]
y = [40, 30, 25, 40, 18, 20, 22, 15]

# Menghitung koefisien beda terbagi
coef = divided_difference(x, y)

# Membuat GUI
root = tk.Tk()
root.title("Interpolasi Newton")

plot_button = tk.Button(root, text="Plot Interpolasi", command=plot_interpolation)
plot_button.pack(padx=20, pady=20)

root.mainloop()