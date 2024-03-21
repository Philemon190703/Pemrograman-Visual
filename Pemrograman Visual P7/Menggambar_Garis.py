import numpy as np
import matplotlib.pyplot as plt

# Titik a dan b
a = (100, 200)
b = (800, 600)

# Menghitung gradien (slope)
m = (b[1] - a[1]) / (b[0] - a[0])

# Menyusun array x dari x1 hingga x2
x_values = np.linspace(a[0], b[0], 1000)

# Menghitung nilai y menggunakan persamaan garis
y_values = m * (x_values - a[0]) + a[1]

# Plot garis menggunakan Matplotlib
plt.plot(x_values, y_values, color='black')
plt.scatter([a[0], b[0]], [a[1], b[1]], color='red')  # Tandai titik a dan b
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Garis yang Melewati Titik a dan b')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
