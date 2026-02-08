import math

def jarak(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) # Math.sqrt() dipake untuk menghitung akar kuadrat
    return d

x1, y1 = 1, 1
x2, y2 = 4, 5

hasil = jarak(x1, y1, x2, y2)

print(f"Jarak = {hasil}")