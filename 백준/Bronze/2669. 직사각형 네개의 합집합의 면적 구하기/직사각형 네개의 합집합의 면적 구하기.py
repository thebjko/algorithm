ls = list(map(int, open(0).read().split()))

x = ls[::2]
y = ls[1::2]

matrix = [[0] * (max(x) - min(x)) for _ in range(max(y) - min(y))]
for p in range(0, len(ls), 4):
    a, b, c, d = map(lambda x: x - 1, ls[p:p + 4])
    a, c = map(lambda z: z - min(x), [a, c])
    b, d = map(lambda z: z - min(y), [b, d])
    for i in range(a, c):
        for j in range(b, d):
            if matrix[j][i] == 0:
                matrix[j][i] = 1 

print(sum(map(sum, matrix)))
