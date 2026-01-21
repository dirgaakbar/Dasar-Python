# Enter pin
print('Tanpa batas')

pin = int(input('Masukkan pin atm kamu:	'))
while pin != 1234:
	pin = int(input('Pin salah, coba lagi:	'))

print('pin benar')

# Enter pin dengan kesempatan
print('3 kali percobaan')

pin = int(input('Masukkan pin atm kamu:	'))
kesempatan = 3
while pin != 1234 and kesempatan > 0:
	kesempatan -= 1
	print(f'Sisa kesempatan {kesempatan}')
	pin = int(input('Pin salah, coba lagi:	')) 

if pin != 1234:
	print('Atm anda terblokir')
else:
	print('Pin benar')
