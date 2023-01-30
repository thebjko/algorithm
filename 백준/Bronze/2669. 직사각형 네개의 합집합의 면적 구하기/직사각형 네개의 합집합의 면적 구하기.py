ls = list(map(int, open(0).read().split()))

matrix = [[0] * max(ls[::2]) for _ in range(max(ls[1::2]))]
for p in range(0, len(ls), 4):
    a, b, c, d = map(lambda x: x - 1, ls[p:p + 4])
    for i in range(a, c):
        for j in range(b, d):
            if matrix[j][i] == 0:
                matrix[j][i] = 1 

print(sum(map(sum, matrix)))
