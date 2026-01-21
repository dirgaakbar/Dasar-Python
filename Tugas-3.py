# Game tebak angka
import random

angka_rahasia = random.randint(1, 10)
tebakan = int(input('Masukkan angka tebakan (1-10):  '))

while tebakan != angka_rahasia:
    tebakan = int(input('Coba lagi:    '))
    if tebakan < angka_rahasia:
        print('Tebakan terlalu kecil')
    elif tebakan > angka_rahasia:
        print('Tebakan terlalu besar')
    else:
        print('Selamat! tebakan kamu benar')
