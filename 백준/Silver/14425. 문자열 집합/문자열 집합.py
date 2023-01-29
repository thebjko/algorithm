from collections import Counter

n, m, *a = open(0).read().split()
n, m = map(int, [n, m])
N = a[:n]
M = a[n:]
c = Counter(M)
print(sum([c[word] for word in N]))