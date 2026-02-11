#soal1
class Produk:
    def __init__(self, nama_produk, harga):
        self.nama_produk = nama_produk
        self.harga = harga

    def info_produk(self):
        return f"Nama Produk: {self.nama_produk}, Harga: Rp{self.harga}"

class ProdukElektronik(Produk):
    def __init__(self, nama_produk, harga, garansi):
        super().__init__(nama_produk, harga)
        self.garansi = garansi  # dalam tahun

    def info_produk(self):
        return (f"Nama Produk: {self.nama_produk}, "
                f"Harga: Rp{self.harga}, "
                f"Garansi: {self.garansi} tahun")

class ProdukMakanan(Produk):
    def __init__(self, nama_produk, harga, tanggal_kadaluarsa):
        super().__init__(nama_produk, harga)
        self.tanggal_kadaluarsa = tanggal_kadaluarsa

    def info_produk(self):
        return (f"Nama Produk: {self.nama_produk}, "
                f"Harga: Rp{self.harga}, "
                f"Tanggal Kadaluarsa: {self.tanggal_kadaluarsa}")
            
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

#soal5
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
