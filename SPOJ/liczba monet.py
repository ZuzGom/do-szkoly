monety = [500, 200, 100, 50, 20, 10, 5, 2, 1]

m = float(input())
m = int(m * 100)
c = 0
h = 0

while True:
    if h > 0:
        break
    for x in monety:
        if m - x > 0:
            m -= x
            c += 1
            break
        if m - x == 0:
            c += 1
            h += 1
            break
    else:
        break
print(c)
