from Parent_Class import *
class Mahasiswa(Person):
        prodi = ""
        semester = ""

def ___init____(self, nama, gender, umur, prodi, semester):
        super(). ___init__(nama, gender, umur)
        self.prodi= prodi
        self.semester = semester

def cetak(self):
        super().cetak()
        print("Prodi\t\t :",self.prodi,
              "\nsemester\t :", self.semester,
              "\n------------------")