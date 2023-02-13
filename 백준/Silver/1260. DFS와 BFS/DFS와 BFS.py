from sys import stdin
from collections import deque

input = stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort(reverse=True)

def dfs(start_vertex: int) -> None:
    explored, stack = set(), [start_vertex]
    while stack:
        v = stack.pop()
        if v not in explored:
            explored.add(v)
            print(v, end=" ")
            for i in graph[v]:
                if i not in explored:
                    stack.append(i)

dfs(V)   # if 줄일 수 없을까?

print()
for i in graph:
    i.sort()

def bfs(start_vertex: int) -> None:
    explored, queue = set(), deque([start_vertex])
    while queue:
        v = queue.popleft()
        if v not in explored:
            explored.add(v)
            print(v, end=" ")
            for i in graph[v]:
                if i not in explored:
                    queue.append(i)

bfs(V)