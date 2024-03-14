import numpy as np
import matplotlib.pyplot as plt

# Ukuran gambar
rowmax = int(500)
colmax = int(500)

# Pusat lingkaran
center_x = int(rowmax / 2)
center_y = int(colmax / 2)

# Radius maksimum lingkaran
radius_max = int(200)

# Batas jarak untuk setiap warna
batas1 = int(0.2 * radius_max)
batas2 = int(0.4 * radius_max)
batas3 = int(0.6 * radius_max)
batas4 = int(0.8 * radius_max)

# Membuat gambar berukuran rowmax x colmax x 3 dengan tipe data int16
Gambar = np.zeros(shape=(rowmax + 1, colmax + 1, 3), dtype=np.int16)

# Mengisi warna pada gambar berdasarkan jarak dari pusat lingkaran
for i in range(0, rowmax + 1):
    for j in range(0, colmax + 1):
        distance = (i - center_x) ** 2 + (j - center_y) ** 2

        if distance >= 0 and distance < batas1 ** 2:
            Gambar[i, j, 0] = 255
        if distance >= batas1 ** 2 and distance < batas2 ** 2:
            Gambar[i, j, 1] = 255
        if distance >= batas2 ** 2 and distance < batas3 ** 2:
            Gambar[i, j, 2] = 255
        if distance >= batas3 ** 2 and distance < batas4 ** 2:
            Gambar[i, j, 0] = 255
            Gambar[i, j, 1] = 255
        if distance >= batas4 ** 2 and distance < radius_max ** 2:
            Gambar[i, j, 0] = 255
            Gambar[i, j, 2] = 255

# Menampilkan gambar
plt.figure()
plt.imshow(Gambar)
plt.show()
