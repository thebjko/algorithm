n, *ls = map(int, open(0).read().split())

weight = ls[::2]
stature = ls[1::2]

min_weight, max_weight = min(weight), max(weight)
min_stature, max_stature = min(stature), max(stature)

matrix = [[0] * (max_weight - min_weight + 1) for _ in range(max_stature - min_stature + 1)]

adj_weight = map(lambda x: x - min_weight, weight)
adj_stature = map(lambda x: x - min_stature, stature)

for w, s in zip(adj_weight, adj_stature):
    matrix[s][w] = 1

for i in range(0, 2 * n, 2):
    w, s = ls[i] - min_weight, ls[i + 1] - min_stature
    rank = sum(map(lambda x: sum(x[w + 1:]), matrix[s + 1:]))
    print(rank + 1, end=" ")