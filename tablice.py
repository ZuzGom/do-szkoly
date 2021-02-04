
while 0 == 0:
    wynik = ''
    linia = list(input())
    for x in linia[::-1]:
        wynik += x
    print(wynik)



'''
line = input().split()
wynik = ''
line = line[::-1]
for x in line:
    wynik += x + ' '
wynik = wynik[:-1]
print(wynik)

#########################3
n = int(input('Liczba liczb: '))
bartosz = []
for i in range(n):
    bartosz.append(input('Wczytaj '+str(i+1)+'. liczbę: '))
bartosz = bartosz[::-1]
print(bartosz)
'''

