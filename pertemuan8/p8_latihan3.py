# File : p8_latihan3.py

class Jurnal:
    tanggal = ''
    uraian = ''
    debet = 0
    kredit = 0

simpan = []

j1 = Jurnal()
j1.tanggal = '22/10/18'
j1.uraian = 'Beli Jajan'
j1.kredit = 90000
simpan.append(j1)


j2 = Jurnal()
j2.tanggal = '23/10/18'
j2.uraian = 'Beli Kopi'
j2.kredit = 25000
simpan.append(j2)

print(simpan[0].uraian)
print(simpan[0].tanggal)

print(simpan[1].uraian)
print(simpan[1].tanggal)

