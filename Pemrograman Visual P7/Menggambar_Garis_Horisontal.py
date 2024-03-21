import numpy as np
import matplotlib.pyplot as plt

# Titik a dan b
a = (100, 200)
b = (1800, 200)

rowmax = int(500)
colmax = int(500)

# Menggambar garis horizontal
y_value = a[1]  # Koordinat y tetap sama untuk garis horizontal

# Plot garis menggunakan Matplotlib
plt.plot([a[0], b[0]], [y_value, y_value], color='black')
plt.scatter([a[0], b[0]], [a[1], b[1]], color='red')  # Tandai titik a dan b
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Garis Horizontal yang Melewati Titik a dan b')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
