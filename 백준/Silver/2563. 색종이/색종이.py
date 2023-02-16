_, *ls = list(map(int, open(0).read().split()))
matrix = [[0] * 101 for _ in ' '*101]

for a, b in zip(ls[::2], ls[1::2]):
    for i in range(10):
        matrix[b+i][a:a+10] = [1]*10

print(sum(map(sum, matrix)))