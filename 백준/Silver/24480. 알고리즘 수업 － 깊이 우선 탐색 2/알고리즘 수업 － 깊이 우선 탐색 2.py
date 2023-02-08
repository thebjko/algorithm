import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
ls = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
ans = ['0'] * n

for _ in range(m):
    a, b = map(int, input().split())
    ls[a].append(b)
    ls[b].append(a)

for i in ls:
    i.sort(reverse=True)

cnt = 0
def dfs(x: int):
    global cnt
    visited[x] = True
    cnt += 1
    ans[x-1] = str(cnt)
    for i in ls[x]:
        if not visited[i]:
            dfs(i)

dfs(r)
print("\n".join(ans))