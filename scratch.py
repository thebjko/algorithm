from math import ceil
a, b, v = map(int, open(0).read().split())
# a + (a - b) * x = v
print(ceil((v - a)/(a - b)) + 1)