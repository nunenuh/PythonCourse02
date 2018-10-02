
class Bidang:
    nama = ''
    seksi = ''


class Kantor:
    nama = ''
    bidang = []

    def tambahBidang(self, bidang):
        self.bidang.append(bidang)

    def ambilBidang(self, index):
        return self.bidang[index]

k1 = Kantor()
k1.nama = 'Dispora'

b1 = Bidang()
b1.nama = 'Kepemudaan'
b1.seksi = 'pembinaan'
k1.bidang.append(b1) 

b2 = Bidang()
b2.nama = 'Olahraga'
b2.seksi = 'kompetisi'
k1.tambahBidang(b2)

# akses langsung ke attribut
print(k1.bidang[0].nama)

print(k1.ambilBidang(0).nama)



