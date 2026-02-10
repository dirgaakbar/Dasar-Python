# Exception adalah kesalahan (error) yang terjadi saat program sedang berjalan (runtime error)

# try: # Kode yang dijalankan dan berpotensi error
# except: # Penangkap & penangan error yang terjadi di dalam try
# finally: # Penutup kode yang PASTI dijalankan, mau terjadi error ataupun tidak
try:
    angka = int(input("Masukkan angka pembagian: "))
    print(10 / angka)
except: # disini letak errorny: ZerodivisionError & TypeError & ValueError
    print('terjadi error')
finally:
    print('Program selesai dijalankan')
