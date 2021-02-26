
def nwd(a,b):
    while a!=b :
        if a>b:
            a-=b 
        else:
            b-=a
    return a

for _ in range(int(input())):
    line = input().split()
    x = int(line[0])
    y = int(line[1])
    d = nwd(x, y)
    print(int(x*y/d))
