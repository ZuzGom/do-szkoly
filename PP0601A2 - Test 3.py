count = 0
big  = 0
last = '42'
while True:
    check =  input()
    print(check)
    if check == '42':
        if last != '42':
            big += 1
    if big >= 3:
        exit()
    last = check
