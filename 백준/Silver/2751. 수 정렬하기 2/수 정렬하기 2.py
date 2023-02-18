from heapq import *
N, *ls = map(int, open(0).read().split())
heapify(ls)
for i in ' '*N:
    print(heappop(ls))