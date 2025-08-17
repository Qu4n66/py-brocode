import random
import string

chars = ' ' + string.punctuation + string.ascii_letters + string.digits




chars = list(chars)

key = chars.copy()


random.shuffle(key)

#print(f'Chars: {chars}')
#print(f'keys: {key}')

ori = input('Enter a message:')

cipher = ''

for letter in ori:
    index = chars.index(letter)
    cipher += key[index]



print(f'Original message: {ori}')
print(f'encrypted message: {cipher}')
#----------------------------------------

cipher = input('Enter a message:')

ori = ''

for letter in cipher:
    index = key.index(letter)
    ori += chars[index]


print(f'encrypted message: {cipher}')
print(f'Original message: {ori}')


