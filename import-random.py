import random
print('Game Tebak Angka')
level = input('Pilih angka (bulat/desimal):    ')
if level == 'bulat':
	angka = random.randint(1, 10)
	tebakan = int(input('Tebak angka 1-10:	'))
	if tebakan == angka:
		print('tebakanmu benar')
	else:
		print(f'tebakanmu salah, yang benar {angka}')

elif level == 'desimal':
	angka =random.uniform(1, 10)
	tebakan = int(input('Tebakan Angka 1-10:  '))
	if tebakan == angka:
		print('tebakanmu benar')
	else:
		print(f'tebakanmu salah, yang benar {angka}')

else:
	print(f'Pilihan tidak valid')
