import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
def lagrange_interpolation(x, y, xi):
    n = len(x)
    result = 0
    
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (xi - x[j]) / (x[i] - x[j])
        result += term
    return result
    
def plot_interpolation():
    x_values = np.linspace(5, 40, 500)
    y_values = [lagrange_interpolation(x, y, xi) for xi in x_values]
 
    plt.scatter(x, y, color='red', label='Data Points')
    plt.plot(x_values, y_values, label='Lagrange Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Lagrange Interpolation')
    plt.legend()
    plt.grid(True)
    plt.show()

# Data contoh
x = [5, 10, 15, 20, 25, 30, 35, 40]
y = [40, 30, 25, 40, 18, 20, 22, 15]

# Membuat GUI
root = tk.Tk()
root.title("Interpolasi Lagrange")
plot_button = tk.Button(root, text="Plot Interpolasi", command=plot_interpolation)
plot_button.pack(padx=20, pady=20)
root.mainloop()