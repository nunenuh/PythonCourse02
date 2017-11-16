# File : p8_latihan5.py

class GradeConverter:
    
    def nilaiToGrade(self, nilai):
        grade = ""
        if nilai >= 90 and nilai <= 100:
            grade = "A"
        elif nilai >= 80 and nilai < 90:
            grade = "B+"
        elif nilai >= 50 and nilai < 80:
            grade = "C"
        elif nilai >= 45 and nilai < 50:
            grade = "D"
        else:
            grade = "DO"
        
        return grade

    def ubahNilai(self, data_nilai):
        data_grade = []
        for nilai in data_nilai:
            grade = self.nilaiToGrade(nilai)
            data_grade.append(grade)
        
        return data_grade


data = [100, 90, 80, 45, 50]
gc = GradeConverter()
print(gc.ubahNilai(data))
print(gc.nilaiToGrade(85))
