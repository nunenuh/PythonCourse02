def cari_grade(a):
    grade = ""
    if a >= 90 and a <= 100:
        grade = "A"
    elif a >= 80 and a < 90:
        grade = "B+"
    elif a >= 70 and a < 80:
        grade = "B"
    elif a >= 60 and a < 70:
        grade = "C+"
    elif a >= 50 and a < 60:
        grade = "C"
    elif a >= 40 and a < 50:
        grade = "D"
    elif a >= 30 and a < 40:
        grade = "E"
    else:
        grade = "DO"
    
    return grade

nilai = int(input("Masukan Nilai Adit : "))
grade = cari_grade(nilai)
print('Grade Adit adalah : ' + grade)