komb = [1, 1, 2]
for i in range(2, 25):
    komb.append(komb[i]+komb[i-1]+komb[i-2])
print(komb)
proba = int(input())

for _ in range(proba):
    m = 1
    for x in input().split():
        m = (m * (komb[int(x)])) % 1000000007
    print(m)

#limit czasu