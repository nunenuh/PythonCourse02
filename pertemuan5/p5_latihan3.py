# File: p5_latihan3.py

# memanggil module os 
# yang merupakan library untuk mengakses sistem operasi
import os

# memanggil module pandas
# yang digunakan untuk mengolah data 
# berbentuk csv, excel dll
import pandas as pd

# untuk mendapatkan lokasi direktori
# tempat file ini bekerja
folder = os.getcwd()

# mencari file yang di inginkan
# yaitu data.csv
file = os.path.join(folder, 'pertemuan5/data.csv')

# untuk memanggil file csv 
# dan mengubah nya menjadi dataframe 
read = pd.read_csv(file)
print(read)

# mengubah csv yang berbentuk dataframe
# menjadi berbentuk record
jurnal = read.to_dict(orient='record')
print(jurnal)


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