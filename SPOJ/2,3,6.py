
ciag = ''

for i in range(1000):
    if i%2==0:
        ciag += 'a'
    if i%3==0:
        ciag += 'b'

#print(ciag)
def ch_quick(nap):
    if len(nap) == 1:
        return 1
    if len(nap) == 2:
        if nap == 'ab' or nap == 'ba':
            return 1
    if len(nap) == 3:
        if nap == 'aba' or nap == 'aba' or nap == 'abb':
            return 1
    if len(nap) == 4:
        if nap == 'abab' or nap == 'baab' or nap == 'aaba':
            return 1
    if len(nap) == 5:
        if nap == 'ababa' or nap == 'abaab' or nap =='baaba' or nap == 'aabab':
            return 1
    return 0

def sprawdz(napis):
    if len(napis) < 6:
        if ch_quick(napis):
            return 1
        else:
            return 0
    for p in range(5):
        if string[p:p+5] == 'ababa':
            break
    else:
        return 0
    if p > 0:
        if not ch_quick(napis[:p]):
            return 0
    k = (len(napis) - p) % 5
    #print(k,p, len(napis))
    if k > 0:
        if 'ababa'[0:k] != napis[len(napis) - k:] or k == 1:
            return 0
    i = 0
    while i < len(napis) - k:
        #print(napis[i:i+5])
        if napis[i:i+5] != 'ababa':
            return 0
        i += 5
    return 1
    
for _ in range(int(input())):
    string = input()
    if sprawdz(string):
        print('tak')
    else:
        print('nie')
