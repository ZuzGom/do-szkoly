monety = [5.00, 2.00, 1.00, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]

m = float(input())
c = 0
h = 0


def przyb(y):
    x = int(y * 1000)
    if x % 10 > 4:
        x += 1
    x = int(x/10)
    return x/100


while True:
    if h > 0:
        break
    for x in monety:
        if m - x > 0:
            m -= x
            m = przyb(m)
            c += 1
            break
        if m - x == 0:
            c += 1
            h += 1
            break
    else:
        break
print(c)
