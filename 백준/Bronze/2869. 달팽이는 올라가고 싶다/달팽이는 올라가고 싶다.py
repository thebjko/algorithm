from math import ceil
a, b, v = map(int, open(0).read().split())
print(ceil((v - a)/(a - b)) + 1)