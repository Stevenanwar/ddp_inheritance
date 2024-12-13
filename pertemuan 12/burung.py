from animal import *

class burung(animal):
    def __init__(self, nama, makanan, hidup, berkembang_Biak, sayap, motif):
        super().__init__(nama, makanan, hidup, berkembang_Biak)
        self.sayap = sayap
        self.motif = motif

    def cetak_burung(self):
        super().cetak()
        print('\nsayap :' , self.sayap)
        print("\nmotif :" , self.motif)

kakatua = burung ('kakatua', 'daging', "darat", 'bertelur', '2' , "hitam putih")
merpati = burung ('merpati', 'biji', "darat", 'bertelur', '2' , "hijau biru")
kakatua.cetak_burung()
print("----------------------------")
merpati.cetak_burung()


