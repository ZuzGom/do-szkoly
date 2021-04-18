tab = [1,2,4,7,9,10,12,16]
beg = 0
end = len(tab)-1
szu = int(input("Szukana: "))
ind = int((end+beg)/2)
c = 0
while szu != tab[ind]:
    if c>len(tab):
        break
    c+=1
    ind = int((end+beg)/2)
    if tab[ind]<szu:
        beg = ind
    elif tab[ind]>szu:
        end = ind
if c>len(tab):
    print("Nie ma liczby w tablicy")
else:
    print("Indeks:",ind)
