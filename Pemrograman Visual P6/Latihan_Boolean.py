# Input nilai a dan b
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))

# Cek apakah a lebih besar dari b
a_lebih_b = a > b

# Cek apakah b lebih besar dari a
b_lebih_a = b > a

# Cek apakah a sama dengan b
a_sama_b = a == b

# Hitung PPN a dan b jika memenuhi syarat
ppn_a = 0
ppn_b = 0

if a > 10000:
    ppn_a = a * 0.12

if b > 50000:
    ppn_b = b * 0.12

# Cek apakah penambahan PPN a dan b lebih besar dari 0
ppn_total_lebih_0 = (ppn_a + ppn_b) > 0

# Hapus a dan b, cek apakah berhasil
del a
del b

# Cek apakah a dan b berhasil dihapus
a_terhapus = "a" not in globals()
b_terhapus = "b" not in globals()

# Output
print("a lebih besar dari b:", a_lebih_b)
print("b lebih besar dari a:", b_lebih_a)
print("a sama dengan b:", a_sama_b)
print("PPN a:", ppn_a)
print("PPN b:", ppn_b)
print("Total PPN lebih dari 0:", ppn_total_lebih_0)
print("a terhapus:", a_terhapus)
print("b terhapus:", b_terhapus)
