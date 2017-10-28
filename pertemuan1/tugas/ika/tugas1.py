# kondisi kasus berhijab maka perempuan else laki-laki
inp = input("Apakah Menggunakan Jilbab? (1/0):")

h = int(inp)

perempuan = bool(h) # True / False

if perempuan:
    print("dia perempuan")
else:
    print("dia laki-laki")