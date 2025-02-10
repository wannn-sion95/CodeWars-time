""" 
kode ini mengubah jumlah detik menjadi format waktu yang mudah dibaca, yaitu jam:menit:detik (HH:MM:SS ).

Fungsi ini berguna untuk menampilkan waktu dalam format yang lebih familiar, seperti pada stopwatch atau timer

"""

def make_readable(seconds):
    if seconds < 0 or seconds > 359999:
        raise ValueError("Input harus diantara 0 - 359999 detik.")
        
    jam = seconds // 3600
    seconds %= 3600
    menit = seconds // 60
    seconds %= 60

    return f"{jam:02d} : {menit:02d} : {seconds:02d}"



print(make_readable(0))
print(make_readable(59))
print(make_readable(60))
print(make_readable(3600))
print(make_readable(359999))
