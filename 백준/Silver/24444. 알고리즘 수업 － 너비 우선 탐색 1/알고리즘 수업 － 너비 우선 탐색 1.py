import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, R = map(int, input().split())
ls = [[] for _ in range(N+1)]
visited = [False] * (N+1)
ans = ['0'] * (N)

for _ in range(M):
    a, b = map(int, input().split())
    ls[a].append(b)
    ls[b].append(a)   

for i in ls:
    i.sort()

cnt = 0
q: deque = deque([R])
def bfs(q: deque) -> None:
    global cnt
    
    if not q:
        return

    v = q.popleft()
    if ans[v - 1] == "0":
        cnt += 1
        ans[v - 1] = str(cnt)
    
    for u in ls[v]:
        if not visited[u]:        
            visited[u] = True
            q.append(u)

    bfs(q)

bfs(q)
print("\n".join(ans))
