print('Skrypt do wyszukiwania nieparzystych miejsc zerowych wielomianu\n')

# krok = float(input('Podaj krok \n(im mniejszy, tym większa dokładność [default::1] ): '))
krok = 0.001
print('\nPodaj wpsółczynniki w formacie: \n\npotęga wpsółczynnik\n\n'
      'kończąc na wyrazie wolnym (0 _) np:\n\n'
      '1 2\n0 3\n\nto 2x^1 + 3\n')

line = ['']
wsp = []
lista = []

while line[0] != '0':
    line = input().split()
    wsp.append(line)

wsp.sort(reverse=True)

nazwa = ''
print('\nTwój wielomian to: ')
for i in range(len(wsp)):
    if i == len(wsp) - 1:
        nazwa += wsp[i][1]
    else:
        nazwa += wsp[i][1] + 'x^' + wsp[i][0] + ' + '
print(nazwa)


def wielomian(v):
    pomoc = 0
    for y in wsp:
        pomoc += int(y[1]) * (v ** int(y[0]))
    return pomoc


end = 100

if int(wsp[0][0]) == 0 and len(wsp) == 1:
    if wsp[0][1] == '0':
        wynik = 'nieskonczenie wiele miejsc zerowych'
    else:
        wynik = 'brak miejsc zerowych'
else:
    check = int(wsp[0][1])
    for i in range(int(wsp[0][0])):
        c = 0  # counter
        if check > 0:  # a > 0, zaczynamy od góry
            while wielomian(end) < 0:
                end += krok
            beg = end - krok
            while wielomian(beg) > 0:
                beg -= krok
                c += 1
                if c > 1000*(1/krok):
                    break
            end = beg + krok

            wynik = (beg + end) / 2

            while wielomian(wynik) != 0:
                if c > 1000*(1/krok):
                    wynik = 'to by było na tyle'
                    print('\n!!!UWAGA!!!')
                    print('Sugeruję zmniejszyć krok')
                    break
                wynik = (beg + end) / 2
                if end == wynik or beg == wynik:
                    break
                if wielomian(wynik) < 0:
                    beg = wynik
                if wielomian(wynik) > 0:
                    end = wynik
            try:
                end = wynik - 0.0001
                if wielomian(wynik-0.0001) < 0:
                    check = - check
            except TypeError:
                print('\nTo by było na tyle')
                break
            else:
                print('\nJeden z pierwiastków to: ')
                wynik = round(wynik, 10)
                print(wynik)
                lista.append(wynik)

        else:  # a < 0, zaczynamy od dołu
            while wielomian(end) > 0:
                end += krok
            beg = end - krok
            while wielomian(beg) < 0:
                c += 1
                if c > 1000*(1/krok):
                    break
                beg -= krok
            end = beg + krok

            wynik = beg

            while wielomian(wynik) != 0:
                if c > 1000*(1/krok):
                    wynik = 'to by było na tyle'
                    print('\n!!!UWAGA!!!')
                    print('Sugeruję zmniejszyć krok')
                    break
                wynik = (beg + end) / 2
                if end == wynik or beg == wynik:
                    break
                if wielomian(wynik) > 0:
                    beg = wynik
                if wielomian(wynik) < 0:
                    end = wynik
            try:
                end = wynik-0.0001
                if wielomian(wynik-0.0001) > 0:
                    check = - check
            except TypeError:
                print('\nTo by było na tyle')
                break
            else:
                print('\nJeden z pierwiastków to: ')
                wynik = round(wynik, 10)
                print(wynik)
                lista.append(wynik)

lista.sort()
print('\nSugerować pierwiastki niewymierne?')
print(lista)
czy = input('y/n: ')
if czy == 'y':
    pierwiastki = [0.4142135624, 0.7320508076, 4, 0.2360679775,
                   0.4494897428, 0.6457513111, 0.8284271247, 9, 0.1622776602,
                   0.3166247904, 0.4641016151, 0.6055512755]
    for p in lista:
        if p < 0:
            i = (-p) % 1
        else:
            i = p % 1
        for x in range(12):
            if pierwiastki[x] == i:
                print('Sugestia dla ' + str(p))
                print('√'+str(x+2))
print('To wszystko')
