
'''
x = 2.3333333333333335
print(('%.8f'%x))
g = float("{:10f}".format(x))
print(g)
'''
T = int(input())
#print(2**(1/2))


for t in range(T):
    n = int(input())
    line = []
    punkty = []
    for _ in range(n):
        line.append(input().split())
    
    for li in line:
        li[0] = float(li[0])
        li[1] = float(li[1])
    #print(line)
    #print(line[1][1]-line[0][1])
    #print(line[0][0]-line[1][0])

    wynik = []

    up = 0


    #for i in range(n)
    for i in range(n):
        #print('i:',i)  
        for h in range(i):
            #print('h:',h)
            x = (line[i][1]-line[h][1])/(line[h][0]-line[i][0])
            x = float('%.5f'%x)
            #x = float("{:5f}".format(x))
            y = line[i][0]*x + line[i][1]
            y = float('%.5f'%y)
            #y = float("{:5f}".format(y))
            punkty.append([x,y])
                
            
     
            
    for g in punkty:
        x = g[0]
        y = g[1]
        #print(x,y)
        print('y:',y)
        for lin in line:
            #szu = float("{:5}".format(lin[0]*x + lin[0]))
            szu = lin[0]*x + lin[1]
            szu = float('%.5f'%szu)
            print(szu)
            if lin[1] > 0:
                if y > szu:
                    break

            else:
                if y < szu:
                    break
        else:
            print('yo')
            wynik.append([x,y])
    print(line)
    print(wynik)
    #print(punkty)
    #punkty.append(punkty[0])
    '''
    
    print(line)
    odleglosc = []
    for _ in range(n-1):
        odleglosc.append([])
    print(odleglosc)

    
    for i in range(len(punkty)):
        check = punkty[i]
        for j in range(len(punkty)):
            print(j)
            d = ((punkty[j][0]-check[0])**2+(punkty[j][1]-check[1])**2)**(1/2)
            odleglosc[j].append(d)
    print(odleglosc)

    '''



    
    
    wynik.append(wynik[0])
    i = 0
    suma = 0
    while i < n-1:
        suma += wynik[i][0]*wynik[i+1][1] - wynik[i+1][0]*wynik[i][1]
        i += 1
    print(suma)
    
    print(punkty)