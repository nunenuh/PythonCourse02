

# Buatlah perulangan dari 0 s / d n.
# Kemudian Tentukan angka tersebut
# genap atau ganjil menggunakan rumus
# nilai % 2 sama dengan 0 // Genap

#Mencari Nilai Genap dan Ganjil
n = int(input('Masukkan jumlah perulangan : '))
n = n + 1

for nilai in range(0, n):
    if nilai % 2 == 0:
        print(str(nilai) + '  = Genap')
    else:
        print(str(nilai) + ' = Ganjil')
    
