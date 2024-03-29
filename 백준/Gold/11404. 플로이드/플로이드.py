from math import inf, isinf
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

# inf = sys.maxsize
matrix = [[inf] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    matrix[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    if c < matrix[a][b]:
        matrix[a][b] = c


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if matrix[a][b] > matrix[a][k] + matrix[k][b]:
                matrix[a][b] = matrix[a][k] + matrix[k][b]

print('\n'.join(' '.join('0' if isinf(val) else str(val) for val in i[1:]) for i in matrix[1:]))