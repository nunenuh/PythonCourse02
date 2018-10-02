# File : p5_latihan2.py

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


out = "tanggal | uraian | debet | kredit"
print(out)

jl = len(jurnal)
for index in range(0,jl):
    tgl = jurnal[index]['tanggal']
    ur = jurnal[index]['uraian']
    db = jurnal[index]['debet']
    kr = jurnal[index]['kredit']

    otx = tgl + ur + str(db) + str(kr)
    ot = tgl + ' | ' + ur + ' | ' + str(db) + ' | ' + str(kr)
    print(ot) 
print('Ini di luar perulangan')
    
    