import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dfs(x, y):
    if field[y][x]:
        field[y][x] = 0
        for dx, dy in delta:
            a, b = x + dx, y + dy
            if 0<=a<M and 0<=b<N:
                dfs(a, b)
        return True

for _ in range(T):
    M, N, K = map(int, input().split())

    field = [[0] * M for _ in ' '*N]

    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1

    cnt = 0
    for i in range(M):
        for j in range(N):
            if dfs(i, j):
                cnt += 1

    print(cnt)
