import sys
from collections import deque
input = sys.stdin.readline
def bfs(q: deque):
    while q:
        u, idx = q.popleft()
        for v in graph[u]:
            if visited[v] == -1:
                q.append((v, idx^1))
                visited[v] = idx^1
                s.discard(v)
            elif visited[v] == idx:
                print('NO')
                return False
    return True

for tc in range(int(input())):
    V, E = map(int, input().split())   # 정점의 개수, 간선의 개수
    graph = [[] for _ in range(V+1)]
    s = set()
    visited = [-1 for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        s.update([u, v])
        graph[u].append(v)
        graph[v].append(u)
    
    while True:
        x = s.pop()
        visited[x] = 0
        f = bfs(deque([(x, 0)]))
        if s and f:   # set이 아직 비지 않았으나 f == True일 때 -> 아직 탐색하지 않은 트리가 있다.
            continue
        elif f:   # set이 비었지만 f == True일 때 -> 다 탐색
            print('YES')   # 'YES' 출력 후 종료
            break
        else:   # set이 비었고 f == False일 경우 'NO'가 이미 출력되었음.
            break