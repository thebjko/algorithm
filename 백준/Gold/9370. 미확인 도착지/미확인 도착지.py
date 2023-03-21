import sys
from heapq import *
from collections import defaultdict
from math import ceil, inf, isinf
input = sys.stdin.readline

for _ in range(int(input())):
    n, m, t = map(int, input().split())   # 교차로(node), 도로(edge), 목적지 후보의 개수
    s, g, h = map(int, input().split())   # 출발지, g -> h 로 지나갔다.
    
    graph = defaultdict(dict[int])
    distance = [inf] * (n+1)
    for _ in range(m):
        a, b, d = map(int, input().split())   # a <-> b, 거리 d
        if {a, b} == {g, h}:
            d -= .01
        graph[a][b] = d
        graph[b][a] = d

    # 데이크스트라
    q = [(0, s)]
    distance[s] = 0
    while q:
        cost, current_node = heappop(q)
        if cost > distance[current_node]:   # 같으면 다른 경로를 선택할 수 있기 때문에 >=가 아니라 >
            continue
        for node_to_proceed, cost_to_next_node in graph[current_node].items():
            cost_to_proceed = cost + cost_to_next_node
            if cost_to_proceed < distance[node_to_proceed]:
                distance[node_to_proceed] = cost_to_proceed
                heappush(q, (cost_to_proceed, node_to_proceed))

    result = set()
    for _ in range(t):
        x = int(input())
        if not isinf(distance[x]) and distance[x] != ceil(distance[x]):
            result.add(x)

    print(*sorted(result))