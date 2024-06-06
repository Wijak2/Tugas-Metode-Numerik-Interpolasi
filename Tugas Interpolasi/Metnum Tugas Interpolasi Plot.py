import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

#interpolasi lagrange
def interpolasiLagrange(x, y, xi):
    n = len(x)
    result = 0
    
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (xi - x[j]) / (x[i] - x[j])
        result += term
    return result
    
def plotLagrange():
    x_values = np.linspace(5, 40, 500)
    y_values = [interpolasiLagrange(x, y, xi) for xi in x_values]
 
    plt.scatter(x, y, color='red', label='Data Points')
    plt.plot(x_values, y_values, label='Interpolasi Lagrange')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolasi Lagrange')
    plt.legend()
    plt.grid(True)
    plt.show()

#Interpolasi Newton
def divided_difference(x, y):
    n = len(x)
    coef = y.copy()

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])

    return coef

def interpolasiNewton(x, coef, xi):
    n = len(x)
    result = coef[n - 1]

    for i in range(n - 2, -1, -1):
        result = result * (xi - x[i]) + coef[i]

    return result

def plotNewton():
    x_values = np.linspace(5, 40, 500)
    y_values = [interpolasiNewton(x, coef, xi) for xi in x_values]

    plt.scatter(x, y, color='red', label='Data Points')
    plt.plot(x_values, y_values, label='Interpolasi Newton')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolasi Newton')
    plt.legend()
    plt.grid(True)
    plt.show()

# Data contoh
x = [5, 10, 15, 20, 25, 30, 35, 40]
y = [40, 30, 25, 40, 18, 20, 22, 15]

coef = divided_difference(x, y)

# Membuat GUI
root = tk.Tk()
root.title("Interpolasi")
plot_button = tk.Button(root, text="Plot Interpolasi Lagrange", command=plotLagrange)
plot_button2 = tk.Button(root, text="Plot Interpolasi Newton", command=plotNewton)
plot_button.pack(padx=70, pady=20)
plot_button2.pack(padx=70, pady=20)
root.mainloop()