# [Silver I] 케빈 베이컨의 6단계 법칙 - 1389 

[문제 링크](https://www.acmicpc.net/problem/1389) 

### 성능 요약

메모리: 33376 KB, 시간: 64 ms

# 코드 분석
## 내 코드 :
```python
from math import inf, isinf

N, M, *ls = map(int, open(0).read().split())
graph = [[inf] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0

for i, j in zip(ls[::2], ls[1::2]):
    graph[i][j] = 1
    graph[j][i] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                graph[j][i] = graph[j][k] + graph[k][i]


def f(ls: list) -> int:
    kb = 0
    for i in ls:
        if not isinf(i):
            kb += i
    return kb


answer = 0
record = inf
for i, j in enumerate(map(f, graph[1:])):
    if j < record:
        record = j
        answer = i

print(answer+1)
```
노드 수가 최대 100이고, 관계가 최대 5000이라서 매트릭스 -> 플로이드 워셜로 접근했다. 각 그래프에 대해 최소값을 가진 노드 번호+1을 출력하면 끝. `f` 함수 대신 `lambda x: sum(i for i in x if not isinf(i))`를 사용할 수도 있다.

<br>

## [mudrhs1991 님의 코드 :](https://www.acmicpc.net/source/54521982)
```python
import sys

n, m = map(int, sys.stdin.readline().split())
board = [[] for _ in range(n)]
visited = [sys.maxsize for _ in range(n)]
result = sys.maxsize
answer = 0

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    board[start-1].append(end-1)
    board[end-1].append(start-1)

def dfs(node, num):
    global result
    if visited[node] <= num:
        return
    visited[node] = num
    for i in board[node]:
        dfs(i, num+1)

for i in range(n):
    dfs(i,0)
    sum = 0
    for j in visited:
        sum += j
    if sum < result:
        result = sum
        answer = i
    visited = [sys.maxsize for _ in range(n)]

print(answer+1)
```
> 메모리 약 31MB, 시간 32ms

DFS로 접근했다. visited에 재귀 깊이를 기록한다. 이전에 방문되었으면 retrn. 각 노드에 dfs를 실행해 최소값을 가진 노드 번호+1 출력.