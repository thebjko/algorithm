for i in [*open(0)]:
    a, b = map(int, i.split())    
    if a == b == 0:
        break
    print(a+b)
    