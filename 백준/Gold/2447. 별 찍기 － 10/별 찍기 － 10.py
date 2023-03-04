n = int(input())
stars = [['*'] * n for _ in range(n)]

def puncher(n: int):
    if n == 1:
        return
    m = n // 3
    s = set([*range(m, 2*m)])
    for i in range(len(stars)):
        if i//m == 1:
            for l in stars[i::n]:
                for j in range(m):
                    l[m+j::n] = [' '] * (len(l)//n)
    puncher(m)

puncher(n)
print(*map(''.join, stars), sep='\n')