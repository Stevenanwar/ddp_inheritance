class animal:
    def __init__(self, nama, makanan, hidup, berkembang_Biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_Biak = berkembang_Biak
    
    def cetak(self):
         print("\nnama :", self.nama)
         print("\nmakanan :", self.makanan)
         print("\nhidup :", self.hidup)
         print("\nberkembang_Biak :", self.berkembang_Biak)

object = animal("buaya", "daging", "amfibi", "bertelor")
object.cetak()
print("------------------------------------------------")

