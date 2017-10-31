# File : p3_latihan2.py
a = [1, 5, 7, 6, 9]
print(a)

# membalik urutan index array
a.reverse()
print(a)

# menambah isi array di bagian paling akhir
a.append(13)
print(a)

# menambah isi array pada index tertentu
angka = 21
index = 1
a.insert(index, angka)
print(a)


# menghapus array berdasarkan index
index = 3
a.pop(index)
print(a)