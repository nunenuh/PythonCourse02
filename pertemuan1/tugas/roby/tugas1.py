# input akan berbentuk text '0' atau '1'
inp = input("Apakah Berhijab (1/0):")

# mengubah text menjadi angka bilangan bulat
h = int(inp)

# mengubah angka bilangan bulat menjadi logika 
# True / False
berhijab = bool(h) # True / False

if berhijab:
    print("Perempuan")
else:
    print("Laki-laki")