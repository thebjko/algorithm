import sys
from itertools import accumulate

input = sys.stdin.readline

n, m = map(int, input().split())
ls = map(int, input().split())

cache = [0] + list(accumulate(ls))

for _ in range(m):
    a, b =  map(int, input().split())
    print(cache[b]-cache[a-1])