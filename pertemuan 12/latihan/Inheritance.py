from subclass1 import *
from subclass2 import*

m1 = Mahasiswa('Siti Aminah', 'Wanita', 20,'SI',3)
m2 = Mahasiswa('Budi Santoso', 'Pria', 23,'SI',5)
d1 = Dosen('Budi Santoso', 'Pria', 23,'SI',5)
d2 = Dosen('Budi Santoso', 'Pria', 23,'SI',5)
# gunakan fungsi2 yang ada di class
d1.setGaji(12000000)
d2.setGaji(10000000)    

m1.cetak()
m2.cetak()
d1.cetak()
d2.cetak()