from collections import Counter
a, b, c = map(int, open(0).read().split())
x = Counter(str(a * b * c))
for i in range(10):
    print(x.get(str(i), 0))