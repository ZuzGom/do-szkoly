print('\nSkrypt do wyszukiwania nieparzystych miejsc zerowych wielomianu\n')

krok = int(input('Podaj krok (im mniejszy, tym większa dokładność): '))

print('\nPodaj wpsółczynniki w formacie: \npotęga_przy_zmiennej wpsółczynnik np:\n\n'
      '1 2\n0 3\n\nto 2x + 3\n\n'
      'kończąc na wyrazie wolnym\n')

line = ['']
wsp = []

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


def wielomian(x):
    pomoc = 0
    for y in wsp:
        pomoc += int(y[1]) * (x ** int(y[0]))
    return pomoc


end = 100

# wielomian(beg)
# wielomian(end)

if int(wsp[0][0]) == 0 and len(wsp) == 1:
    if wsp[0][1] == '0':
        wynik = 'nieskonczenie wiele miejsc zerowych'
    else:
        wynik = 'brak miejsc zerowych'
else:
    check = int(wsp[0][1])
    for i in range(int(wsp[0][0])):
        c = 0  # counter
        if check > 0:
            while wielomian(end) < 0:
                end += krok
            beg = end - krok
            while wielomian(beg) > 0:
                beg -= krok
                c += 1
                if c > 1000:
                    break
            end = beg + krok

            wynik = (beg + end) / 2

            while wielomian(wynik) != 0:
                if c > 1000:
                    wynik = 'to by było na tyle'
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
                print(wynik)

        else:
            while wielomian(end) > 0:
                end += krok
            beg = end - krok
            while wielomian(beg) < 0:
                c += 1
                if c > 1000:
                    break
                beg -= krok
            end = beg + krok

            wynik = beg

            while wielomian(wynik) != 0:
                if c > 1000:
                    wynik = 'to by było na tyle'
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
                print(wynik)
