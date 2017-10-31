#File : p3_latihan6.py

# mendefinisikan variabel jurnal 
# sebagai array tidak berisi nilai
jurnal = []

b1 = {
    'tanggal': '22/10/17',
    'uraian': 'Beli Jajan',
    'debet': 0,
    'kredit': 10000
}
# memasukan dictionary b1 kedalam array jurnal
# dengan index ke 0
jurnal.append(b1)

b2 = {
    'tanggal': '23/10/17',
    'uraian': 'Jual Pakaian',
    'debet': 50000,
    'kredit': 0
}
# memasukan dictionary b2 kedalam array jurnal
# dengan index ke 1
jurnal.append(b2)

b3 = {
    'tanggal': '25/10/17',
    'uraian': 'Beli Kupi',
    'debet': 0,
    'kredit': 20000
}
# memasukan dictionary b3 kedalam array jurnal
# dengan index ke 2
jurnal.append(b3)


# mencetak baris pertama
baris = 0 # baris pertama
print(jurnal[baris])

# mencetak baris kedua
baris = 1 # baris kedua
print(jurnal[baris])

# mencetak baris ketiga dengan isi kolom uraian
baris = 2 # baris ketiga
kolom = 'uraian' # nama kolomnya
print(jurnal[baris][kolom])



