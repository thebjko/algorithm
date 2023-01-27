# 절댓값 힙
from heapq import heapify, heappush, heappop

heapify(ls := [])
for num in [*open(0)][1:]:
    num = int(num)
    if num != 0:
        heappush(ls, (abs(num), num))
    elif ls:
        print(heappop(ls)[1])
    else:
        print(0)
