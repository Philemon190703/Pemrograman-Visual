makanan_set = {"nasi", "sate", "gado-gado", "rendang"}
print("Masukkan makanan:", makanan_set)
print("Panjang set makanan:", len(makanan_set))
makanan_set.add("mie goreng")
print("Makanan setelah menambahkan 'mie goreng':", makanan_set)
makanan_set.update(["soto", "bakso"])
print("Makanan setelah menambahkan 'soto' dan 'bakso':", makanan_set)
makanan_set.remove("sate")
print("Makanan setelah menghapus 'sate':", makanan_set)
makanan_set.discard("nasi")
print("Makanan setelah menghapus 'nasi' dengan discard:", makanan_set)

elemen_terhapus = makanan_set.pop()
print("Elemen yang dihapus dari makanan:", elemen_terhapus)
print("Masukkan makanan setelah menghapus elemen secara acak dengan pop:", makanan_set)

makanan_set.clear()
print("Masukkan makanan setelah menghapus semua elemen dengan clear:", makanan_set)

makanan_set1 = {"nasi", "sate", "gado-gado"}
makanan_set2 = {"rendang", "mie goreng", "soto"}
makanan_union = makanan_set1.union(makanan_set2)
print("Union dari dua set makanan:", makanan_union)

print("\nPembelian Makanan:")
print("A: Hai, saya ingin memesan beberapa makanan.")
print("B: Tentu, apa yang ingin Anda pesan?")
print("A: Saya ingin pesan", len(makanan_union), "macam makanan.")
print("B: Baik, apa saja yang Anda inginkan?")
print("A: Saya ingin pesan", makanan_union)
print("B: Baik, pesanan Anda akan segera diproses.")