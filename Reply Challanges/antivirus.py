
import sys
import time
sys.stdout = open('anti_out.txt', 'w')
f = open('input-antivirus-4193.txt', 'r')

start = time.process_time()
def check(s):
    c = 0
    indices = []
    wynik = [[],[],[],[]]
    inde = 0
    for j in range(4):
        indices.append([i for i, x in enumerate(roz[j]) if x == s])
        if j == 0:
            pomo = len(indices[0])
        if len(indices[j])<pomo:
            inde = j
            pomo = len(indices[j])
    

    def sprawdz(cze):
        for i in range(4):

            for j in range(len(indices[i])):
                x = indices[i][j]
                if files[i][x:x+m] == cze:
                    break
            else:
                return False
        return True

    for p in range(pomo):
        hel=files[inde][indices[inde][p]:indices[inde][p]+m]
        if sprawdz(hel):
            c = 1
            for i in range(4):

                for j in range(len(indices[i])):
                    x = indices[i][j]
                    if files[i][x:x+m] == hel:
                        wynik[i]=x
            break
    else: 
        return 0, wynik
                
    return c, wynik


for t in range(int(f.readline())):
    lon = f.readline().split()
    m = int(f.readline())
    files = []
    for _ in range(4):
        files.append(f.readline())

    pref = [[0],[0],[0],[0]]
    roz = [[],[],[],[]]
    kubel = []
    for _ in range(26*m):
        kubel.append(0)

    for i in range(4):
        suma = 0
        j = 0
        while j < int(lon[i]):
            suma += ord(files[i][j])-96    
            pref[i].append(suma)
            if j >= m:
                roz[i].append(pref[i][j]-pref[i][j-m])
            j+= 1
        roz[i].append(pref[i][j]-pref[i][j-m])

    for x in roz:
        pomoc = set(x)
        for y in pomoc:
            kubel[y] += 1
    szuk = [i for i, x in enumerate(kubel) if x == 4]

    for szu in szuk:

        c, indi = check(szu)
        if c != 0:
            break

    print('Case #'+str(t+1)+':', end=' ')

    for x in indi:
        print(x, end=' ')
    print('\n', end='')

print(time.process_time() - start)
