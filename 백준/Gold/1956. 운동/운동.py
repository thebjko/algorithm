import sys
input = sys.stdin.readline

v, e = map(int, input().split())
road = [[int(1e9) for i in range(v)] for j in range(v)]
result = int(1e9)

for i in range(v):
    road[i][i] = 0

for i in range(e):
    a, b, c = map(int, input().split())
    road[a - 1][b - 1] = c

for i in range(v):
    for j in range(v):
        for k in range(v):
            road[j][k] = min(road[j][k], road[j][i] + road[i][k])

for i in range(v):
    for j in range(v):
        if i != j and road[i][j] != int(1e9) and road[j][j] != int(1e9):
            result = min(result, road[i][j] + road[j][i])

print(result if result != int(1e9) else -1)