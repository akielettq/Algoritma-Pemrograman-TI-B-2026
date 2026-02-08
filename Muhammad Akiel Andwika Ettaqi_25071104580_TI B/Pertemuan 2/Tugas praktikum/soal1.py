def rata_rata(nilai):
    if len(nilai) == 0:
     return "Data kosong"
    else:
     rata = sum(nilai) / len(nilai)
     return rata
    
mahasiswa1 = [80, 75, 90, 60, 85] # Jika sesuai

print(rata_rata(mahasiswa1))

mahasiswa2 = [] # Jika kosong

print(rata_rata(mahasiswa2))