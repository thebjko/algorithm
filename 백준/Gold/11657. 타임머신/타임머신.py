import sys

input = sys.stdin.readline

N, M = map(int, input().split())

edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

inf = int(1e9)

dist = [inf] * (N+1)
dist[1] = 0
negative_cycle_exists = False
for i in range(N):
    for j in range(M):
        current_node = edges[j][0]
        next_node = edges[j][1]
        cost = edges[j][2]

        if dist[current_node] != inf and dist[next_node] > dist[current_node] + cost:
            dist[next_node] = dist[current_node] + cost

            if i == N-1:
                negative_cycle_exists = True

if negative_cycle_exists:
    print(-1)
else:
    for i in range(2, N+1):
        if dist[i] == inf:
            print(-1)
        else:
            print(dist[i])