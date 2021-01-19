print('Podaj wpsółczynniki w formacie: \npotęga_przy_zmiennej wpsółczynnik np:\n'
      '1 2\n0 3\nto 2x + 3\n'
      'kończąc na wyrazie wolnym')

line = ['']
wsp = []

while line[0] != '0':
    line = input().split()
    wsp.append(line)

wsp.sort(reverse=True)

nazwa = ''
print('Twój wielomian to: ')
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


if int(wsp[0][1]) == 0 and len(wsp) == 1:
    if wielomian(end) == 0:
        wynik = 'nieskonczenie wiele miejsc zerowych'
    else:
        wynik = 'brak miejsc zerowych'
else:
    if int(wsp[0][1]) > 0:
        while wielomian(end) < 0:
            end += 10
        beg = end - 10
        while wielomian(beg) > 0:
            beg -= 10
        end = beg + 10
        print(beg)
        print(end)

        wynik = (beg + end)/2

        while wielomian(wynik) != 0:
            wynik = (beg + end) / 2
            if wielomian(wynik) < 0:
                beg = wynik
            if wielomian(wynik) > 0:
                end = wynik
            print(wielomian(wynik))

    else:
        while wielomian(end) > 0:
            end += 10
        beg = end - 10
        while wielomian(beg) < 0:
            beg -= 10
        end = beg + 10
        print(beg)
        print(end)

        wynik = beg

        while wielomian(wynik) != 0:
            wynik = (beg + end) / 2
            if wielomian(wynik) > 0:
                beg = wynik
            if wielomian(wynik) < 0:
                end = wynik
            print(wynik)

print('wynik')
print(wynik)
