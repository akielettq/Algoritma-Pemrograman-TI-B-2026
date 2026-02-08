def pangkat_rekursif(a, b):
    if b == 0:
        return 1
    else:
        return a * pangkat_rekursif(a, b - 1)

a = 2
b = 5
hasil = pangkat_rekursif(a, b)

print(f"Input: a = {a}, b = {b}")
print(f"Output: {hasil}")