from math import inf, isinf

n, m, *ls = open(0)
n = int(n)
m = int(m)


matrix = [[inf] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    matrix[i][i] = 0

for i in ls:
    a, b, c = map(int, i.split())
    matrix[a][b] = min(matrix[a][b], c)


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            matrix[a][b] = min(matrix[a][b], matrix[a][k] + matrix[k][b])


for i in matrix[1:]:
    for val in i[1:]:
        print(0 if isinf(val) else val)