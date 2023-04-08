from heapq import *

N, M, *ls = map(int, open(0).read().split())
s = set(str(i) for i in ls)

if N == 100:
    print(0)
    exit()

if M == 10:
    print(abs(N-100))
    exit()

heap = [(0, N)]
for i in range(0, 10**6):
    str_i = str(i)
    for j in str_i:
        if j in s:
            break
    else:
        heappush(heap, (min(abs(i-100), len(str_i)), abs(N-i)+100))

while heap:
    cost, cur = heappop(heap)
    if cur == 100:
        print(cost)
        break
    heappush(heap, (cost + abs(cur-100), 100))