import sys
sys.stdout = open('Party_out.txt', 'w')
f = open('input.txt')

n = int(f.readline())

for i in range(n):
    fr = int(f.readline())
    friends = f.readline().split()
    beauty = 0
    for x in friends:
        if int(x) > 0:
            beauty += int(x)
    print('Case #'+str(i+1)+': '+str(beauty))

sys.stdout.close()
