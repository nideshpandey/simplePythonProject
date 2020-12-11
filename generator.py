import random
import string

LETTERS = string.ascii_letters
DIGITS = string.digits


length = input('Enter length to be made')
length = int(length)

def password_generator(length):
    temp_password = f'{LETTERS}{DIGITS}'
    shuffled = list(temp_password)
    random.shuffle(shuffled)
    password = random.choices(shuffled, k = length)
    password = ''.join(password)
    return password

new_password = password_generator(length)

print(new_password)
