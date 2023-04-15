from math import inf, isinf

N, M, *ls = map(int, open(0).read().split())
graph = [[inf] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0

for i, j in zip(ls[::2], ls[1::2]):
    graph[i][j] = 1
    graph[j][i] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                graph[j][i] = graph[j][k] + graph[k][i]


def f(ls: list) -> int:
    kb = 0
    for i in ls:
        if not isinf(i):
            kb += i
    return kb


answer = 0
record = inf
for i, j in enumerate(map(f, graph[1:])):
    if j < record:
        record = j
        answer = i

print(answer+1)