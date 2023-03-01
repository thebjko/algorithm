import io, os, sys


input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def is_bipartite(ls: list):
    while ls:
        u, idx = ls.pop()
        for v in graph[u]:
            if visited[v] == -1:
                ls.append((v, idx^1))
                visited[v] = idx^1
                s.discard(v)
            elif visited[v] == idx:
                print('NO')
                return
    if s:
        x = s.pop()
        visited[x] = 0
        is_bipartite([(x, 0)])
    else:
        print('YES')
        return


for tc in range(int(input())):
    V, E = map(int, input().split())   # 정점의 개수, 간선의 개수
    graph = [[] for _ in range(V+1)]
    s = set()   # 모든 그래프가 탐색되었는지 확인하기 위한 세트
    visited = [-1] * (V+1)   # 방문 표시할 리스트
    
    # 그래프 그리기
    for _ in range(E):
        u, v = map(int, input().split())
        s.update([u, v])
        graph[u].append(v)
        graph[v].append(u)
    
    # 전처리 및 bfs 수행
    x = s.pop()
    visited[x] = 0
    is_bipartite([(x, 0)])