
data = ['adit', 'cai', 'roby', 'ika']

def tambah_data(nama):
    data.append(nama)
    print(data)

def hapus_data(idx):
    data.pop(idx)
    print(data)

def proses():
    status = 'Y'
    while status == 'Y':
        print('Pilih Menu : ')
        print('1. Tambah Data')
        print('2. Hapus Data')

        pilihan = int(input('Masukkan No. Menu Yang dipilih : '))

        if pilihan == 1:
            nama = input('Masukkan Nama : ')
            tambah_data(nama)
        elif pilihan == 2:
            print(data)
            idx = int(input('Masukkan data yang akan dihapus : '))
            hapus_data(idx)
        else:
            print('Pilih antara 1 atau 2')
        
        status = input('Apakah anada ingin mengulang lagi Y/N : ')

proses()
