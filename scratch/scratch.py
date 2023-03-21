import io, os, sys
from heapq import *
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input = io.BytesIO(os.read('input.txt', os.fstat('input.txt').st_size)).readline

inf = float('inf')
for _ in range(int(input())):
    n, m, t = map(int, input().split())   # 교차로(node), 도로(edge), 목적지 후보의 개수
    s, g, h = map(int, input().split())   # 출발지, g -> h 로 지나갔다.
    
    graph = [[] for _ in range(n+1)]
    distance = [inf] * (n+1)
    for _ in range(m):
        a, b, d = map(int, input().split())   # a <-> b, 거리 d
        graph[a].append((b, d))
        graph[b].append((a, d))

    # 데이크스트라
    q = [(0, s)]
    distance[s] = 0
    while q:
        cost, current_node = heappop(q)
        if cost > distance[current_node]:   # 같으면 다른 경로를 선택할 수 있기 때문에 >=가 아니라 >
            continue
        for node_to_proceed, cost_to_next_node in graph[current_node]:
            if current_node in {g, h} and node_to_proceed not in {g, h}:
                continue
            cost_to_proceed = cost + cost_to_next_node
            if cost_to_proceed < distance[node_to_proceed]:
                distance[node_to_proceed] = cost_to_proceed
                heappush(q, (cost_to_proceed, node_to_proceed))

    result = []
    for _ in range(t):
        x = int(input())   # 목적지 후보
        if distance[x] != inf:
            result.append(distance[x])

    print(*sorted(result))
            