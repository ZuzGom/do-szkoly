try:
    s = int(input())
except Exception as e:
    print(type(e), e)
    print('niepoprawny format daty')