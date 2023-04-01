## [kito4972 님의 코드 :](https://www.acmicpc.net/source/56069192)
```python
import sys;import heapq;input=sys.stdin.readline;from collections import deque;
V, E = map(int, input().split())
INF = 1 << 31
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, c = map(int, input().split()) # 0 < c <= 10000
    graph[u].append((v, c))

def dijkstra2():
    pq = []
    dist = [[INF for _ in range(V+1)] for _ in range(V+1)]
    ans = INF
    for source in range(1, V+1):
        for adj, cost in graph[source]:
            dist[source][adj] = cost
            heapq.heappush(pq, (cost, source, adj))
    while pq:
        shortest, source, current = heapq.heappop(pq)
        if source == current: return  shortest
        if shortest > dist[source][current]: continue

        for adj, cost in graph[current]:
            new_cost = shortest+cost
                # ans = min(ans, new_cost)
                # dist[source][adj] = new_cost
            if dist[source][adj] > new_cost:
                dist[source][adj] = new_cost
                heapq.heappush(pq, (new_cost, source, adj))
    return -1
print(dijkstra2())
```
> 메모리 약 83MB, 시간 588ms

