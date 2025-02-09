"""
Kode ini mengecek apakah tiga angka dapat membentuk segitiga menggunakan aturan
bahwa jumlah dua sisi harus lebih besar dari sisi ketiga, serta memastikan bahwa semua sisi memiliki panjang lebih besar dari nol.
""" 

def is_triangle(a: int, b:int, c:int) ->bool:
    if a + b > c and a + c >  b and b + c > a:
        return a > 0 and b > 0 and c > 0
    return False

print(is_triangle(1, 2, 2))
print(is_triangle(4, 2, 3))
print(is_triangle(2, 2, 2))
print(is_triangle(1, 2, 2))
print(is_triangle(-5, 1, 3))
print(is_triangle(0, 2, 3))
print(is_triangle(1, 2, 9))

