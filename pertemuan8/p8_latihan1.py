# File : p8_latihan1.py

class Rumus:

    def luas_segitiga(self, a,t):
        return 1/2 * a * t

    def luas_persegi(self, s):
        return s*s

class Rumus2:
    # atribute (variable)
    pi = 3.14

    # method (fungsi)
    def luas_lingkaran(self, r):
        return self.pi * r *r


r = Rumus()
seg = r.luas_segitiga(10,5)
per = r.luas_persegi(10)

r2 = Rumus2()
ling = r2.luas_lingkaran(10)
print(ling)
