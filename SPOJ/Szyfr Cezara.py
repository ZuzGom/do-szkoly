alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
           'P', 'R', 'S', 'T', 'U', 'W', 'Y', 'Z']


def cezar(wyraz):
    fraktal = 'FRAKTAL'
    try:
        if len(fraktal) != len(wyraz):
            return False
        ix = alfabet.index(wyraz[0])
        c = ix - 5
        for i in range(len(wyraz)):
            if alfabet.index(wyraz[i]) - alfabet.index(fraktal[i]) != c:
                return False
    except ValueError:
        return False
    else:
        return True


t = int(input())
for _ in range(t):
    wyr = input()
    if cezar(wyr):
        print('tak')
    else:
        print('nie')
