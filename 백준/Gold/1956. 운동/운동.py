import sys
from heapq import *

input = sys.stdin.readline

V, E = map(int, input().split())

distances = [[float('inf')] * (V+1) for _ in range(V+1)]
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def d():
    q = []
    for u in range(1, V+1):
        for v, cost in graph[u]:
            heappush(q, (cost, u, v))
            distances[u][v] = cost

    while q:
        cost, u, v = heappop(q)
        if v == u:
            exit(print(cost))
        if cost < distances[u][v]:   # 같으면 이미 방문해했다는 뜻
            distances[u][v] = cost
        for next_node, cost_to_next in graph[v]:
            total_cost = cost + cost_to_next
            if total_cost < distances[u][next_node]:    # 같으면 넘어가도된다. 이미 방문했다는 뜻.
                heappush(q, (total_cost, u, next_node))
                distances[u][next_node] = total_cost   # 왜? 가장 짧은 거리인지 확인해야 하지 않나?
                                                       # 현재노드까지 가장 짧은 거리로 도착했으니
                                                       # 현재노드에서 다음 노드로 가는게 가장 짧다?
                                                       # 그게 아니라 더 짧은 거리가 있으면 갱신될 것
                                                       # 32번 줄을 주석처리 해도 통과가 되긴 한다.
    
    print(-1)
    
d()