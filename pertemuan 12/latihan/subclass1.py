from Parent_Class import *
class Dosen (Person):
    gelar =""
    jabatan =""
    gaji = 0

    def __init__(self, name, gender, umur, gelar, jabatan):
        super().__init__(name, gender, umur)
        self.gelar = gelar
        self.gender = gender
        
    def setGaji(self, uang):
        self.gaji += uang

    def cetak(self):
        super().cetak()
        print  ("Gelar \t\t :", self.gender,
              "\nJabatan \t :", self.jabatan,
              "\nGaji\t\t : Rp.", self.gaji,
              "\n----------------------------------")