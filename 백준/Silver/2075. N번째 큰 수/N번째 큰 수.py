import sys
from heapq import *

input = sys.stdin.readline
N = int(input())
heap = []
for _ in range(N):
    for i in map(int, input().split()):
        heappush(heap, i)
    
    while len(heap) > N:
        heappop(heap)

print(heappop(heap))
