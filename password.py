import random

haslo = ''

d = int(input('Długość hasła: '))

while len(haslo) < d:
    haslo += chr(random.randint(33, 125))
    haslo = ''.join(set(list(haslo)))

print(haslo)
