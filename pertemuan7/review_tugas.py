

#- Saya memiliki data sebagai berikut
#data = [100, 90, 80, 45, 50]
#contohnya: [100 -> A, 90 -> A, 80 -> B+, 45 -> D, 50 -> C]
#Ketentuan :- Buatlah 2 buah fungsi
#            - fungsi pertama untuk mencari grade nilai
 #           - fungsi kedua untuk mengubah nilai dalam array menjadi sebuah grade
#Output :
#[A, A, B+, D, C]

def cari_grade(a):
    grade = ""
    if a >= 90 and a <= 100:
        grade = "A"
    elif a >= 80 and a < 90:
        grade = "B+"
    elif a >= 50 and a < 80:
        grade = "C"
    elif a >= 45 and a < 50:
        grade = "D"
    else:
        grade = "DO"
    
    return grade

def ubah_nilai(data_nilai):
    data_grade = []
    for nilai in data_nilai:
        grade = cari_grade(nilai)
        data_grade.append(grade)
    
    return data_grade

data = [100, 90, 80, 45, 50]
hasil = ubah_nilai(data)
print(hasil)