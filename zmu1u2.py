liczba = int(input('Podaj w dziesientnym: '))

bity = int(input('Na ilu bitach: '))
uj = 0
if liczba < 0:
    uj = 1
    liczba = -liczba
while 2**(bity-1) < liczba:
    print('Za mało bitów')
    bity = int(input('Na ilu bitach: '))
wagi = []
i = 0
while i < bity:
    wagi.append(2 ** i)
    i += 1
wagi = wagi[::-1]
sum = 0
wynik = []
for i in wagi:
        if sum + i <= liczba:
            sum += i
            wynik.append(1)
        else:
            wynik.append(0)

u1 = ''
for x in wynik:
    if x == 1:
        u1 += '0'
    if x == 0:
        u1 += '1'

u2 = []

i = len(wynik) - 1
while i > 0:
    if wynik[i]==1:
        break
    else:
        u2.insert(0,wynik[i])
    i -= 1
u2.insert(0,wynik[i])
i-= 1

while i >= 0:
    if wynik[i] == 1:
        u2.insert(0,0)
    if wynik[i] == 0:
        u2.insert(0,1)
    i -= 1

wynik[0] = uj
u2[0]=uj

print('ZM:',end=' ')
for x in wynik:
    print(x, end='')
print('\n', end='')
print('U1:',u1)
print('U2:',end=' ')

for x in u2:
    print(x, end='')