import sys
sys.setrecursionlimit(10**6)

i, *ls = open(0)

n, m = map(int, i.split())

parent = [*range(n+1)]

def find(x: int) -> int:
    if parent[x] != x:
        parent[x] = find(parent[x])   # 왜 이렇게?
    return parent[x]

def union(a: int, b: int):
    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for i in ls:
    if i[0] == '0':
        union(*map(int, i[2:].split()))
    else:
        a, b = map(int, i[2:].split())
        print('YNEOS'[find(a) != find(b)::2])   # 왜 이렇게 2