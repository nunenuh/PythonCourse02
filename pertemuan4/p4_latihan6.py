

status = 'Y'
while status == 'Y':
    a = int(input('Masukkan Nilai Panjang : '))
    b = int(input('Masukkan Nilai Lebar : '))
    c = a * b
    print('Hasilnya adalah : ' + str(c))

    print('')
    status = input('Apakah anda ingin menghitung lagi? Y/T : ')

print('Terima Kasih!!!')
