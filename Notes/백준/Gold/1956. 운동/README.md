# [Gold IV] 운동 - 1956 

[문제 링크](https://www.acmicpc.net/problem/1956) 

# 코드 분석
## [kito4972 님의 코드](https://www.acmicpc.net/source/56069192)를 참조해 다시 만들었다.
```python
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
```
> 메모리: 82404 KB, 시간: 552 ms

1. 400개의 거리 테이블을 만들고 한번에 `heapq`에 넣어서 가장 짧은 거리가 최대한 빨리 나오도록 한다.
2. 다익스트라 알고리즘의 조건에 대해선 주석을 참고.
3. 39번째 줄 `distances[u][next_node] = total_cost`을 생략해도 통과가 되긴 하나 시간이 756ms로 더 오래 걸리고 메모리도 101MB가량 요구된다. 왜일까?
    - 통과가 되는 이유는 33, 34번째 줄에서 조건이 체크되기 때문일 것이고, 성능이 더 낮아진 이유는 조건을 39번줄에서 거르지 않으면 heapq의 길이가 더 늘어나기 때문일 것이라 추측한다.