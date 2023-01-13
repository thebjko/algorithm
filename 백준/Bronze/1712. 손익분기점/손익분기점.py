a, b, c = map(int, open(0).read().split())

try:
    p = a / (c - b) + 1
except ZeroDivisionError:
    p = -1

if (p := int(p)) > 0:
    print(p)
else:
    print(-1)
