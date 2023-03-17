import sys
from heapq import *
from math import inf, isinf

input = sys.stdin.readline

V, E = map(int, input().split())   # 노드, 간선의 개수
K = int(input())   # 출발점
graph = [[] for _ in range(V+1)]
distance = [inf] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))   # u에서 v로 가는 비용 w

q = []
heappush(q, (0, K))   # 시작점에서 K로 가는 비용. 시작점이 K이므로 비용 = 0
distance[K] = 0
while q:
    dist_from_K, current_node = heappop(q)
    if distance[current_node] < dist_from_K:   # 이미 기록된 비용이 더 적을 경우
        continue
    for v, w in graph[current_node]:   # 현재 노드와 연결된 다른 노드들과 비용
        cost = dist_from_K + w   # K에서 현재 노드까지 오는 비용 + 현재 노드에서 w로 가는 비용
        if cost < distance[v]:   # K에서 현재 노드를 거쳐 가는 비용이, 거치지 않고 가는 비용보다 더 작으면
            distance[v] = cost   # 거쳐가는 비용으로 업데이트
            heappush(q, (cost, v))   # K에서 v까지 가는 새로운 비용으로 push

print(*[i if not isinf(i) else 'INF' for i in distance[1:]])