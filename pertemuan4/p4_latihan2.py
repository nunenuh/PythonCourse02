

a = int(input('Masukkan Jumlah Perulangan : '))
a = a + 1 #a=16

for var in range(0, a):
    if var == 9:
        print('Berhenti Gerak!')
        break
    else:
        print(str(var) + " Jalan!!!!")

print('Boleh Pulang!')
