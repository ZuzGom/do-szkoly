liczba = int(input('Podaj w dziesientnym: '))

wagi = []
i = 0
v = 0
while v < liczba:
    v = 2 ** i
    wagi.append(v)
    i += 1
wagi = wagi[::-1]
sum = 0
wynik = ''
for i in wagi:
        if sum + i <= liczba:
            sum += i
            wynik += '1'
        else:
            wynik += '0'

print('Liczba w dwójkowym:',wynik)
