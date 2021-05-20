def check(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True

perm = []
#for i in range(256,512):
for i in range(1025):
    perm.append(str(bin(i))[2:])
suma = 0
all = []
for x in perm:
    if (x[0]!='0'):
        all.append(x+x[::-1])
        all.append(x+'0'+x[::-1])
        all.append(x+'1'+x[::-1])

for x in all:
    
    temp = str(int(x,2))
    #print(temp)
    if check(temp) and int(temp)<1000000:
        suma += int(temp)
        print(temp, "\t", x)

print("suma:","\t",suma)


