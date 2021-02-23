max = 0
zysk = 0
for _ in range(int(input())):
    m = int(input())
    zysk += m
    if zysk < 0:
        zysk = 0
    if zysk > max:
        max = zysk
print(max)
