a = input("Masukan Nilai A : ")
a = int(a)

b = input("Masukan Nilai B : ")
b = int(b)

c = (a>=10)
d = (b>=20)

print("A: "+str(c))
print("B: "+str(d))

if c and d:
    print("A AND B = 1")
else:
    print("A AND B = 0")

if c or d:
    print("A OR B = 1")
else:
    print("A OR B = 0")