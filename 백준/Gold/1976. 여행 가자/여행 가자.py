import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

parent = [*range(N+1)]


def union(a: int, b: int):
    while a != parent[a]:
        parent[a] = parent[parent[a]]
        a = parent[a]
        
    while b != parent[b]:
        parent[b] = parent[parent[b]]
        b = parent[b]

    if a != b:
        if a > b:
            a, b = b, a
        parent[b] = a


for i in range(1, N+1):
    for j, k in enumerate(map(int, input().split()), 1):
        if k:
            union(i, j)

if len(set(parent[i] for i in map(int, input().split()))) > 1:
    print('NO')
else:
    print('YES')
