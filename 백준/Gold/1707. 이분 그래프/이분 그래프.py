import sys
input = sys.stdin.readline
def bfs(q: list):
    while q:
        u, idx = q.pop()
        for v in graph[u]:
            if visited[v] == -1:
                q.append((v, idx^1))
                visited[v] = idx^1
                s.remove(v)
            elif visited[v] == idx:
                print('NO')
                return
    if s:
        x = s.pop()
        visited[x] = 0
        bfs([(x, 0)])
    else:
        print('YES')
        return

for tc in range(int(input())):
    V, E = map(int, input().split())   # 정점의 개수, 간선의 개수
    graph = [[] for _ in range(V+1)]
    s = set()
    visited = [-1] * (V+1)
    for _ in range(E):
        u, v = map(int, input().split())
        s.update([u, v])
        graph[u].append(v)
        graph[v].append(u)
    
    x = s.pop()
    visited[x] = 0
    bfs([(x, 0)])