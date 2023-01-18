from math import ceil
a, b, v = map(int, open(0).read().split())
# a + (a - b) * x = v
print(ceil((v - a)/(a - b)) + 1)
print(1-(a-v)//(a-b))
print(1+(v-a)//(a-b))
print(1-(a-v)/(a-b))
print(1+(v-a)/(a-b))