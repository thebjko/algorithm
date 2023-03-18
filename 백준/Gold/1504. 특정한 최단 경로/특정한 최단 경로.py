from math import inf, isinf
from heapq import heappop, heappush


a, *ls = open(0)
n, e = map(int, a.split())
graph = [[] for _ in range(n+1)]

for i in ls[:-1]:
    a, b, c = map(int, i.split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, ls[-1].split())

# 다익스트라 알고리즘
def dijkstra(start: int, end: int) -> int:
    heap, visited = [(0, start)], set()
    while heap:
        cost_from_start_node, current_node = heappop(heap)
        if current_node in visited:
            continue
        visited.add(current_node)
        if current_node == end:
            return cost_from_start_node
        for node_to_proceed, cost in graph[current_node]:
            if node_to_proceed in visited:
                continue
            cost_to_proceed = cost_from_start_node + cost
            heappush(heap, (cost_to_proceed, node_to_proceed))

    return inf


result = min([
    dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n),
    dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n),
])

print(-1 if isinf(result) else result)

"""
https://www.acmicpc.net/board/view/106196
4 5
1 2 100
1 3 1
2 3 1
2 4 10
3 4 1
1 2
"""