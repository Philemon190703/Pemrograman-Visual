#Case 1
f = bool(True)
g = bool(False)
print(f)
print(g)
print("==================================")

#Case 2
print(3>2)
print(3+2==5)
print(3<2)
print("==================================")

#Case 3
print("Case 3")
Penghasilan = 20000000
PenghasilanTanpaPajak = 4000000
if Penghasilan <= PenghasilanTanpaPajak:
    PajakYangHarusDibayar = 0
if Penghasilan > PenghasilanTanpaPajak:
    PajakYangHarusDibayar = 0.1 * Penghasilan
print("Pajak Yang harus anda bayar : Rp ", PajakYangHarusDibayar)

#Case 4
print("Case 4")
a = 3
b = "Ini data string"
c = ("laptop", "buku", "ballpen")
d = ["laptop", "buku", "ballpen"]
e = {"laptop":"asus", "buku":"buku_teks", "ballpen": "arrow"}
f = {1, 2, 3, 4, 5}
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
print("==================================")

#Case 5
print("Case 5")
a = 0
b = ""
c = ()
d = []
e = {}
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print("==================================")

#Case 6
print("Case 6")
class myclass():
    def __len__(self):
        return 0
print(bool(myclass()))
print("==================================")