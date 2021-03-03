
cyf = []
liczba = input('Liczba w 16tkowym: ')
for x in liczba:
    try:
        cyf.append(int(x))
    except ValueError:
        cyf.append(ord(x)-55)
print(cyf)

wynik = ""

wagi = [8,4,2,1]
for x in cyf:
    sum = 0
    for i in wagi:
        if sum + i <= x:
            sum += i
            wynik += '1'
        else:
            wynik += '0'
print(wynik)
