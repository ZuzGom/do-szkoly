print('Podaj wpsółczynniki w formacie: \npotęga_przy_zmiennej wpsółczynnik np:\n'
      '1 2\n0 3\nto 2x + 3\n'
      'kończąc na wyrazie wolnym')

line = ['']
wsp = []

while line[0] != '0':
    line = input().split()
    wsp.append(line)

wsp.sort(reverse=True)
print(wsp)
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

print(wielomian(1))
print(wielomian(-1))