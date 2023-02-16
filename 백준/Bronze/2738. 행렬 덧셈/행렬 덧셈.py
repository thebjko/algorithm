a, *ls = open(0)
N, M = map(int, a.split())
for i in range(N):
    ls[i::N] = map(lambda x: list(map(int, x.split())), ls[i::N])
    for j in range(M):
        print(ls[i::N][0][j] + ls[i::N][1][j], end=' ')