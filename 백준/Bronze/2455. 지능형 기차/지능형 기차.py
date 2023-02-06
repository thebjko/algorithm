import sys

input = sys.stdin.readline

r = 0
ls = []
for _ in range(4):
    a, b = map(int, input().split())
    r -= a
    ls.append(r)
    r += b
    ls.append(r)

print(max(ls))