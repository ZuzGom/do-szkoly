import sys
sys.stdout = open('Score_out.txt', 'w')
f = open('input-scoreboard-7ee1.txt', 'r')

T = int(f.readline())

zadania = []


def Sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if sub_li[j][1] > sub_li[j + 1][1]:
                tempo = sub_li[j]
                sub_li[j] = sub_li[j + 1]
                sub_li[j + 1] = tempo
    return sub_li


for l in range(T):

    line = f.readline().split()
    punkty = []
    zadania = []
    for j in range(int(line[0])):
        punkty.append([0, 0, j+1])
        zadania.append([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

    for _ in range(int(line[1])):
        log = f.readline().split()
        team = int(log[1])
        if log[4] == '1':
            if zadania[team - 1][int(log[2])-1][int(log[3])-1] == 0:
                punkty[team - 1][0] += int(log[3])*100
                punkty[team - 1][1] += int(log[0])
            zadania[team - 1][int(log[2]) - 1][int(log[3]) - 1] = 1

    punkty.sort(reverse=True)
    ch = -1
    wynik = []

    lst2 = [lst[0] for lst in punkty]
    i = 0
    while i < len(punkty):

        if lst2.count(punkty[i][0]) > 1:
            a = lst2.index(punkty[i][0])
            b = next(k for k in reversed(range(len(lst2))) if punkty[k][0] == punkty[i][0])
            bruh = punkty[a:b+1]
            bruh.sort(key=lambda x: x[2])
            bruh.sort(key=lambda x: x[1])
            punkty[a:b + 1] = bruh
            for x in bruh:
                wynik.append(x[2])
            i = b

        else:
            wynik.append(punkty[i][2])
        i += 1
    #print(punkty)
    print('Case #'+str(l+1)+':', end=' ')

    for x in wynik:
        print(x, end=' ')
    print('\n', end='')
f.close()
sys.stdout.close()