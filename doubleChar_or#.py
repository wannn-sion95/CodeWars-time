def solution(s):
    # Jika panjang string ganjil, tambahkan '_'
    if len(s) % 2 != 0:
        s += '#'
    
    # Buat daftar pasangan dua karakter
    return [s[i:i+2] for i in range(0, len(s), 2)]

# Contoh penggunaan , 
print(solution("abc"))    
print(solution("abcdefg"))  
