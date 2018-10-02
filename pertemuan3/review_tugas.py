persons = []

b1 = {
    'no': 5,
    'nama': 'Roby',
    'gender': 'Laki-laki',
    'email': 'rorasnovandama@gmail.com',
}
# memasukan dictionary b1 kedalam array person
# dengan index ke 0
persons.append(b1)

b2 = {
    'no': 10,
    'nama': 'Nurhasanah',
    'gender': 'Perempuan',
    'email': 'nurhasanah@gmail.com',
}
# memasukan dictionary b2 kedalam array person
# dengan index ke 1
persons.append(b2)

b3 = {
    'no': 30,
    'nama': 'Rodi Akbar',
    'gender': 'Laki-laki',
    'email': 'rodiakbar@gmail.com',
}
# memasukan dictionary b3 kedalam array person
# dengan index ke 2
persons.append(b3)

# mencetak baris pertama dengan isi kolom email
inputan = int(input('Masukkan No. Urut yang akan dicari : '))

person = {}
status = False
for item in persons:
    if item['no'] == inputan:
        person = item
        status = True
        break

if status == False:
    print('')
    print('Data tidak ditemukan')
    print('')
else:
    print('')
    print('Data ditemukan : ' + str(person))
    print('')
    inputan_kolom = input('Masukkan nama kolom : ')
    print(person[inputan_kolom])
