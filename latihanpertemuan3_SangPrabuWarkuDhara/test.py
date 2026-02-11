from myOOP import ProdukElektronik, ProdukMakanan, Notifikasi, Email, SMS, Mahasiswa

elektronik = ProdukElektronik("Laptop", 10000000, 2)
makanan = ProdukMakanan("Roti", 15000, "12-03-2026")
notif1 = Email()
notif2 = SMS()
notif3 = Notifikasi()
mhs = Mahasiswa()
print("==================================================")
print("A. INHERITANCE (Pewarisan)")
print("==================================================")
print(elektronik.info_produk())
print(makanan.info_produk())

print("==================================================")
print("B. POLYMORPHISM")
print("==================================================")
print(notif1.kirim())
print(notif2.kirim())
print(notif3.kirim())

print("==================================================")
print("C. ENCAPSULATION")
print("==================================================")
print(mhs.set_nilai(85))
print("Nilai:", mhs.get_nilai())

print(mhs.set_nilai(120))
print("Nilai:", mhs.get_nilai())

