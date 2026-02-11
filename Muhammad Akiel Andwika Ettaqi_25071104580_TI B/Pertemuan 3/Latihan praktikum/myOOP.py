# INHERITANCE (Pewarisan)

class Produk:
    def __init__(self, nama, harga):
        self.nama_produk = nama
        self.harga = harga
    
    def info_produk(self):
        return(f"Nama produk ini adalah {self.nama_produk}, dan harganya adalah {self.harga}")

class ProdukElektronik(Produk):
    def __init__(self, nama, harga, garansi):
        super().__init__(nama, harga)
        self.garansi = garansi
    
    def info_produk(self):
        return f"Nama produk ini adalah {self.nama_produk}, harganya {self.harga}, dan garansi {self.garansi} tahun"
    
class ProdukMakanan(Produk):
    def __init__(self, nama, harga, tanggal):
        super().__init__(nama, harga)
        self.tanggal_kadaluarsa = tanggal

    def info_produk(self):
        return f"Nama produk ini adalah {self.nama_produk}, harganya {self.harga}, dan kadaluarsa tanggal {self.tanggal_kadaluarsa}"


# POLYMORPHISM

class Notifikasi:
    def kirim(self):
        return("hellooooo")

class Email:
    def kirim(self):
        return("Mengirim notifikasi melalui email")

class SMS:
    def kirim(self):
        return("Mengirim notifikasi melalui SMS")

# ENCAPSULATION

class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama
        self.__nilai = 0

    def set_nilai(self, nilai):
        if 0 <= nilai <= 100:
            self.__nilai = nilai
        else:
            return("Nilai tidak valid")
    
    def get_nilai(self):
        return self.__nilai