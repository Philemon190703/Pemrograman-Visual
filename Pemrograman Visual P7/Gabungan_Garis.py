import numpy as np
import matplotlib.pyplot as plt

# Titik a dan b untuk garis vertikal
a_vert = (100, 200)
b_vert = (100, 1000)

# Titik a dan b untuk garis horizontal
a_horiz = (100, 200)
b_horiz = (1800, 200)

# Titik a dan b untuk garis diagonal
a_diag = (100, 200)
b_diag = (800, 600)

# Plot garis menggunakan Matplotlib
plt.figure(figsize=(19.20, 10.80))  # Menyesuaikan ukuran row dan kolom

# Garis vertikal
plt.plot([a_vert[0], b_vert[0]], [a_vert[1], b_vert[1]], color='red', label='Garis Vertikal')

# Garis horizontal
plt.plot([a_horiz[0], b_horiz[0]], [a_horiz[1], b_horiz[1]], color='blue', label='Garis Horizontal')

# Garis diagonal
plt.plot([a_diag[0], b_diag[0]], [a_diag[1], b_diag[1]], color='green', label='Garis Diagonal')

# Tandai titik a dan b untuk garis-garis tersebut
plt.scatter([a_vert[0], b_vert[0], a_horiz[0], b_horiz[0], a_diag[0], b_diag[0]],
            [a_vert[1], b_vert[1], a_horiz[1], b_horiz[1], a_diag[1], b_diag[1]],
            color=['red', 'red', 'blue', 'blue', 'green', 'green'])

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Garis-garis yang Melewati Titik a dan b')
plt.grid(True)
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
