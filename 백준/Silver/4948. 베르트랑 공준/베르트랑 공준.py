from math import ceil, sqrt

for i in map(int, open(0).read().split()):
    if i == 0:
        break
    
    m, n = i, i * 2
    ls = [False] + [True] * ((n - 1) // 2)
    for x in range(1, ceil(sqrt(n) / 2)):
        if ls[x]:
            ls[2*x*x+2*x::2*x+1] = [False] * len(ls[2*x*x+2*x::2*x+1])

    if m == 2 or 2 == n:
        print(1)
    else:
        print(sum(ls[(m+1)//2:]))