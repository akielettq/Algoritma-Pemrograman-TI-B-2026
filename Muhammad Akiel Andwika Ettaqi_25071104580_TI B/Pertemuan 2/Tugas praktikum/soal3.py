def jumlah_digit(n):
    if n < 10: 
        return n  
    else:
        return (n % 10) + jumlah_digit(n // 10)

input_angka = 1234
hasil = jumlah_digit(input_angka)

print(f"Input: {input_angka}")
print(f"Output: {hasil}")