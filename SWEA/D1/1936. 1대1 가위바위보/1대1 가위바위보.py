a, b = input().split()

if ord(a) - ord(b) == 2:
    print('B')
elif int(b) - int(a) == 2:
    print('A')
elif a > b:
    print('A')
elif a < b:
    print('B')