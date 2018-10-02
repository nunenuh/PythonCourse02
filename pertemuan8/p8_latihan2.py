# File : p8_latihan2.py

class Manusia:
    gender = ''
    ras = ''

    def makan(self):
        print("Manusia "+self.gender+ " " +self.ras+" makan")
    
    def minum(self):
        print("Manusia "+self.ras+" minum")

class Pegawai(Manusia):
    nama = ''
    jabatan = ''

    def pekerjaan(self):
        print(self.nama+' bekerja sebagai '+self.jabatan)
    

m = Manusia()
m.gender = 'Pria'
m.ras = 'Indonesia'
m.makan()
m.minum()

p = Pegawai()
p.nama = 'Fandi'
p.jabatan = 'Pengajar'
p.gender = 'Pria'
p.pekerjaan()
p.makan()



