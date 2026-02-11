print("==================================================")
print("A. INHERITANCE (Pewarisan)")
print("==================================================")
#soal1
class produk:
    def __init__(self, nama_produk, harga):
        self.nama_produk = nama_produk
        self.harga = harga

    def printnama(self):
        print("barang =", self.nama_produk, "harga =", self.harga)


#soal2
class produkelektro(produk):
    def __init__(self, nama_produk, harga, tahun):
        super().__init__(nama_produk, harga)
        self.tahun = tahun

    def informasi(self):
        print(self.nama_produk, "seharga", self.harga,"dengan garansi", self.tahun, "tahun")

class makanan(produk):
    def __init__(self, nama_produk, harga, tahun):
        super().__init__(nama_produk, harga)
        self.tahun = tahun

    def info(self):
            print(self.nama_produk, "seharga", self.harga, "kadaluarsa", self.tahun)

b1 = produk("indomie", 3000)
b2 = produkelektro("lampu", 200000, 3)
b3 = makanan("sarden", 15000, "12-02-2030")

b1.printnama()
b2.informasi()
b3.info()


print("==================================================")
print("B. POLYMORPHISM")
print("==================================================")
#soal1
class Notifikasi:
    def kirim(self):
        return "Mengirim notifikasi umum"
#soal4
class Email(Notifikasi):
    def kirim(self):
        return "Mengirim notifikasi melalui Email"

class SMS(Notifikasi):
    def kirim(self):
        return "Mengirim notifikasi melalui SMS"

notif1 = Email()
notif2 = SMS()
notif3 = Notifikasi()

print(notif1.kirim())
print(notif2.kirim())
print(notif3.kirim())

print("==================================================")
print("C. ENCAPSULATION")
print("==================================================")

class Mahasiswa:
    def __init__(self):
        self.__nilai = 0

    def set_nilai(self, nilai):
        if 0 <= nilai <= 100:
            self.__nilai = nilai
            return "Nilai berhasil disimpan"
        else:
            return "Nilai tidak valid"

    def get_nilai(self):
        return self.__nilai

mhs = Mahasiswa()

print(mhs.set_nilai(85))
print("Nilai:", mhs.get_nilai())

print(mhs.set_nilai(120))
print("Nilai:", mhs.get_nilai())
