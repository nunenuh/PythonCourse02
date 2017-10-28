# menghitung segitiga
# contoh kasus : hitung luas segitiga yang panjang alasnya 6 cm dan tingginya 7 cm?
# jawab: luas segitiga = 1/2 x 6 cm x 7 cm = 21 cm2

# inputan dari terminal

# bagian ini tidak di perlukan 
setengah = input("Nilai Rumus1:")

# input nya keteragan alas
alas = input("Nilai Rumus2:")

# input nya keterngan tinggi
tinggi = input("Nilai Rumus3:")

# proses 
# pengisian nilai variabel
# koreksi: cukup tulis 0.5
# tidak diperlukan menulis konstanta pada variabel
a = float(1/2) 

al = int(alas)
ti = int(tinggi)

# operasi logika variabel
# koreksi: cukup tulis 0.5*a1*t1
# koreksi: tidak perlu di beri kurung
luas = (a*al*ti) 


#mencetak hasil variabel
out1 = "luas = a*al*ti = " + str(luas)
print(out1)


