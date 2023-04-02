ls = [(1, 0), (0, 1), (1, 1)]
_, *a = map(int, open(0).read().split())
for i in range(1, max(a)):
    ls.append(tuple(i+j for i, j in zip(ls[i], ls[i+1])))
    
for i in a:
    print(*ls[i])