# Program python dengan input membuat kalkulator sederhana
angka1 = float(input('Angka Pertama:    '))
operator = input('Pilih operator (+, -, *, /)    ')
angka2 = float(input('Angka Kedua:    '))
if operator == '+':
    print(angka1 + angka2)

elif operator == '-':
    print(angka1 - angka2)

elif operator == '*':
    print(angka1 * angka2)

elif operator == '/':
    print(angka1 / angka2)

else:
	print('invalid')
