

def cek_nilai_genap_atau_ganjil(nilai):
    if nilai % 2 == 0:
        return 'Nilai ' + str(nilai) + ' = genap'
    else:
        return 'Nilai ' + str(nilai) + ' = ganjil'

nilai = int(input('Masukkan Nilai : '))
hasil = cek_nilai_genap_atau_ganjil(nilai)
print(hasil)
