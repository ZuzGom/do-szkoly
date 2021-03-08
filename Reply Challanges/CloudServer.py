import sys
sys.stdout = open('serv_out.txt', 'w')
#import time

#start = time.time()


#-server-04f1
f = open('input.txt', 'r')

T = int(f.readline())

for t in range(T):
    line = f.readline().split()
    n = int(line[0])
    p = int(line[1])
    wynik = []

    serv = f.readline().split()

    for i in range(n):
        serv[i]=int(serv[i])
        if i>0:
            serv[i]+=serv[i-1]
    # i = 1

    #rządzę się:
    maxI=-1
    maxJ=-1
    odleglosc=-1

    j=0
    odj=0
    for i in range(n):
        if i>0:
            odj=serv[i-1]

        while (serv[j]-odj)<p and j+1<n:
            j+=1

        temp = (serv[j]-odj) - p
        if  odleglosc == -1:
            maxI=i
            maxJ=j
            odleglosc=temp
        elif temp<odleglosc and temp >= 0:
            maxI=i
            maxJ=j
            odleglosc=temp
        if temp == 0:
            break
    print('Case #' + str(t + 1) + ':', maxI, maxJ)
sys.stdout.close()
