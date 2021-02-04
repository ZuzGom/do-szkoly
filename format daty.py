
n = int(input())

miesiac = ["stycznia", "lutego", "marca",
               "kwietnia", "maja", "czerwca",
               "lipca", "sierpnia", "wrzesnia",
               "pazdziernika", "listopada", "grudnia"]

dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for _ in range(n):
    data = input()
    if len(data) != 8:
        print('niepoprawny format daty')
    else:
        try:
            for i in data:
                s = int(i)
        except ValueError:
            print('niepoprawny format daty')
        else:
            rok = int(data[4:8])
            m = int(data[2:4])
            d = int(data[:2])
            if m > 12 or d < 1 or m < 1 or (not 1000 <= rok <= 2200):
                print('niepoprawny format daty')
            else:
                if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
                    dni[1] += 1
                    if dni[int(m - 1)] < d:
                        print('niepoprawny format daty')
                    else:
                        print(str(d) + ' ' + miesiac[m - 1] + ' ' + str(rok))
                    dni[1] -= 1

                else:
                    if dni[int(m - 1)] < d:
                        print('niepoprawny format daty')
                    else:
                        print(str(d) + ' ' + miesiac[m - 1] + ' ' + str(rok))

# limit czasu KURWA
