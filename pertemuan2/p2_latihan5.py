# jika ada sate kambing
    # maka pesan 2 porsi
    # jika ada jus alpukat
        # maka pesan 3 gelas
    # jika tidak jus alpukat
        # maka pesan air mineral

# jika tidak ada sate kambing
    # maka pesan ayam bakar
    # jika ada jus jeruk
        # maka pesan 2 gelas
    # jika tidak ada jus jeruk
        # maka pesan air mineral


makan = input("Makanan : ")
if makan=='sate-kambing':
    print("Pesan 2 Porsi Sate Kambing")
    minum = input("Minuman : ")
    if minum=='jus-alpukat':
        print("Pesan 3 Gelas Jus Alpukat")
    else:
        print("Gak ada mas, Pesan Air Mineral saja!")
else:
    print("Gak ada mas, Pesan Ayam Bakar saja!")
    minum = input("Minuman : ")
    if minum=='jus-jeruk':
        print("Pesan 2 Gelas Jus Jeruk")
    else:
        print("Gak ada mas, Pesan Air Mineral saja!")