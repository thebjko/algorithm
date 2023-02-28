import sys
from collections import deque
input = sys.stdin.readline

Y, X = map(int, input().split())
route = []
visited = [v1:=[], v2:=[]]
for _ in range(Y):
    route.append(list(map(int, input().rstrip())))
    v1.append([0] * X)
    v2.append([0] * X)

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
q = deque([(0, 0, 1)])
visited[1][0][0] = 1
while q:
    x, y, c = q.popleft()
    if (x, y) == (X-1, Y-1):
        print(visited[c][y][x])
        exit()
    for dx, dy in delta:
        a, b = x+dx, y+dy
        if 0<=a<X and 0<=b<Y and visited[c][b][a] == 0:
            if route[b][a] == 1 and c == 1:
                q.append((a, b, 0))
                visited[0][b][a] = visited[c][y][x] + 1
            elif route[b][a] == 0:
                q.append((a, b, c))
                visited[c][b][a] = visited[c][y][x] + 1

print(-1)