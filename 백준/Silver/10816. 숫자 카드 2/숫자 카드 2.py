from collections import Counter
n, *ls = list(map(int, open(0).read().split()))
counter = Counter(ls[:n])
for i in ls[n+1:]:
    print(counter.get(i, 0))