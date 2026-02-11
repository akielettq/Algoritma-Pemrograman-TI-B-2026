import myOOP as my

# Tes program inheritance

tv = my.ProdukElektronik("TV", 3000000, 2)
print(tv.info_produk())

roti = my.ProdukMakanan("Roti", 15000, "12-12-2026")
print(roti.info_produk())

# Tes program polymorphism

hp1 = my.Notifikasi()
hp2 = my.Email()
hp3 = my.SMS()


print(hp1.kirim())
print(hp2.kirim())
print(hp3.kirim())

# Tes program encapsulation

akiel = my.Mahasiswa("Akiel")
pesan_akiel = akiel.set_nilai(100)

if pesan_akiel:
    print(f"Info {akiel.nama}: {pesan_akiel}")
else:
    print(f"Nilai {akiel.nama} berhasil diisi: {akiel.get_nilai()}")

alam = my.Mahasiswa("Alam")
pesan_alam = alam.set_nilai(1000) # Coba set nilai 1000

if pesan_alam:
    print(f"Info {alam.nama}: {pesan_alam}") 
else:
    print(f"Nilai {alam.nama} berhasil diisi: {alam.get_nilai()}")