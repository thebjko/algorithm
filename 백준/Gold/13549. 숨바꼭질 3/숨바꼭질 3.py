from heapq import *


start, end = map(int, input().split())

if start >= end:
    print(start-end)
    exit()
    
if end == 1:
    print(1)
    exit()

graph = {start: [(start+i, j) for (i, j) in [(-1, 1), (1, 1), (start, 0)] if 0 <= start+i < 100_001]}

# 데이크스트라
def d(start: int, end: int):
    heap = [(0, start)]
    while heap:
        cost_from_start, current_node = heappop(heap)
        if current_node == end:
            print(cost_from_start)
            return 
        while graph[current_node]:
            next_node, cost = graph[current_node].pop()
            if next_node in graph:   # if next_node is already visited
                continue
            c = cost_from_start + cost
            graph[next_node] = []
            for i, j in [(-1, 1), (1, 1), (next_node, 0)]:
                if 0 <= next_node+i < 100_001:
                    graph[next_node].append((next_node+i, j))
            
            heappush(heap, (c, next_node))

d(start, end)