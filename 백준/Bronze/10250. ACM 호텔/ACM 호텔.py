from math import ceil
for _ in range(int(input())):
    h, _, n = map(int, input().split())
    x = ceil(n / h)
    y = h - (h * x - n)
    print(y * 100 + x)