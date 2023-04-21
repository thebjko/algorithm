from heapq import *
_, *ls = map(int, open(0).read().split())
q = []
for i in ls:
    if i:
        heappush(q, i)
    else:
        if q:
            print(heappop(q))
        else:
            print(0)