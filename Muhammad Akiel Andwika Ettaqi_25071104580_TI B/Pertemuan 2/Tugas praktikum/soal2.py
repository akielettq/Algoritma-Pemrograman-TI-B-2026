def bilangan_prima(n):
    list_prima = []
    
    for angka in range(1, n + 1):
        
        if angka > 1:  # Bilangan prima harus lebih dari 1
            adalah_prima = True
            
            for i in range(2, angka):
                if (angka % i) == 0:
                    adalah_prima = False # Bilangan prima hanya habis dibagi dirinya sendiri dan 1
                    break
            
            if adalah_prima:
                list_prima.append(angka)
                
    return list_prima

hasil = bilangan_prima(50)

print(hasil)