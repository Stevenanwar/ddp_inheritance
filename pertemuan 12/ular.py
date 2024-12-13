from animal import *

class ular(animal):
    def __init__(self, nama, makanan, hidup, berkembang_Biak, racun, motif):
        super().__init__(nama, makanan, hidup, berkembang_Biak)
        self.racun = racun
        self.motif = motif

    def cetak_ular(self):
        super().cetak()
        print('\nracun :' , self.racun)
        print("\nmotif :" , self.motif)

sawah = ular ('ular_sawah', 'semut', 'hutan_amazon', 'bertelur', 'berbisa' , "batik kalimantan")
python = ular ('ular_python', 'bayi', 'hutan_ui', 'bertelur', 'berbisa' , "batik afrika")
sawah.cetak_ular()
print("------------------------------------------------")
python.cetak_ular()


