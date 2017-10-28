# File: p1_latihan5.py

# input akan berbentuk text '0' atau '1'
inp = input("Apakah Hujan (1/0):")

# mengubah text menjadi angka bilangan bulat
h = int(inp)

# mengubah angka bilangan bulat menjadi logika 
# True / False
hujan = bool(h) # True / False

if hujan==True:
    print("Saya tidak ke kampus")
else:
    print("Saya Ke Kampus")