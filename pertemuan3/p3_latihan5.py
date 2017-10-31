# File : p3_latihan5.py

dc = {
    'nama': 'Fandi',
    'gender': 'Pria',
    'email': 'nunenuh@gmail.com',
    'alamat': 'Mataram',
    'hoby': 'Memanah, Membaca, Meneliti',
    'lahir': [24, 10, 1988]
}

# yang tercetak adalah fandi
print(dc['nama']) 

# yang tercetak adalah Mataram
print(dc['alamat']) 
# menampilkan isi lahir berbentuk array
print(dc['lahir']) 

# mencetak dictionary lahir 
# dan isi array pada index ke 0
print(dc['lahir'][0])

