
#File : p3_latihan4.py
tanggal = ['22/10/17','23/10/17','25/10/17']
uraian = ['Beli Jajan', 'Jual Pakaian', 'Beli Kupi']
debet = [0, 50000, 0]
kredit = [10000, 0, 20000]

jurnal = [tanggal, uraian, debet, kredit]

#tampilkan baris ke 1 semua isinya
row = 1
tgl = jurnal[0][row]
ur = jurnal[1][row]
db = jurnal[2][row]
kr = jurnal[3][row]

out = tgl + ", " + ur + ", " + str(db) +", " + str(kr)
print(out)

# Tampilkan baris ke 2 kolom kredit
print(jurnal[3][2])