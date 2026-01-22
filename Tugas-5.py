# Guess number codedex
tries = 1
guess = int(input('Guess the number between 1-10:   '))

while guess != 5 and tries < 5:
    print(f'you have {tries} tries')
    guess = int(input('Guess again: '))
    tries += 1

if guess != 5:
    print('you ran out of tries')
else:
    print('you got it')
