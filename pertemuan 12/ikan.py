from animal import *

class ikan(animal):
    def __init__(self, nama, makanan, hidup, berkembang_Biak, jenis, motif):
        super().__init__(nama, makanan, hidup, berkembang_Biak)
        self.jenis = jenis
        self.motif = motif

    def cetak_ikan(self):
        super().cetak()
        print('\njenis :' , self.jenis)
        print("\nmotif :" , self.motif)

cupang = ikan('cupang', 'pelet', "air", 'bertelur', 'bagan' , "oren putih")
hiu = ikan("hiu","daging", "air", "bertelur", "megalodon", "hitam")
cupang.cetak_ikan()
print("----------------------------")
hiu.cetak_ikan()


