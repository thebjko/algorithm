# 데이크스트라
from heapq import *
_, _, *ls = map(int, open(0).read().split())

snl = [[] for _ in range(101)]
for start, dest in zip(ls[::2], ls[1::2]):
    snl[start].append(dest)

def get_destination(start: int) -> int:
    if not snl[start]:
        return start
    return get_destination(*snl[start])

graph = []
for i in range(101):
    graph.append([(i, 0)])
    graph[i] += [(get_destination(j), 1) for j in range(i+1, i+7) if j < 101]

def dijkstra(start: int, end: int) -> int:
    heap = [(0, start)]
    visited = set()
    while heap:
        cost, current = heappop(heap)  # 시작점에서 현재노드까지 가는 비용, 현재노드
        if current in visited:
            continue
        visited.add(current)
        if current == end:   # 현재 노드가 도착점이라면 비용 반환
            return cost
        for v, c in graph[current]:
            if v in visited:
                continue
            cost_to_proceed = cost + c   # 시작점에서 현재 노드까지 오는 비용 + 현재 노드에서 다음 노드로 가는 비용
            heappush(heap, (cost_to_proceed, v))

print(dijkstra(1, 100))