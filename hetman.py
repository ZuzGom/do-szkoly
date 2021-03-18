s = int(input("Rozmiar szachownicy (jeden int): "))

poz = input("Podaj pozycję (dwa inty po spacji): ").split()
x = int(poz[0])
y = int(poz[1])

suma = 2*(s-1)



#licze przekotne od pozycji do:

# lewy gorny 
if s - y > x - 1:
    suma += x - 1
else:
    suma += s - y
# lewy dolny
if y - 1 > x - 1:
    suma += x - 1
else:
    suma += y - 1 
#prawy dolny
if s - x > y - 1:
    suma += y - 1
else:
    suma += s - x

#prawy górny
if s - x > s - y:
    suma += s - y
else:
    suma += s - x

print(suma)