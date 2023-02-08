# [Silver II] 알고리즘 수업 - 깊이 우선 탐색 1 - 24479 

[문제 링크](https://www.acmicpc.net/problem/24479) 

### 성능 요약

메모리: 68732 KB, 시간: 1224 ms

### 분류

깊이 우선 탐색(dfs), 그래프 이론(graphs), 그래프 탐색(graph_traversal), 정렬(sorting)

### 문제 설명

<p>오늘도 서준이는 깊이 우선 탐색(DFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.</p>

<p><em>N</em>개의 정점과 <em>M</em>개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 <em>N</em>번이고 모든 간선의 가중치는 1이다. 정점 <i>R</i>에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.</p>

<p>깊이 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 <strong>오름차순</strong>으로 방문한다.</p>

<pre>dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 <strong>오름차순</strong>으로 방문한다)
        if (visited[x] = NO) then dfs(V, E, x);
}</pre>

### 입력 

 <p>첫째 줄에 정점의 수 <em>N</em> (5 ≤ <em>N</em> ≤ 100,000), 간선의 수 <em>M</em> (1 ≤ <em>M</em> ≤ 200,000), 시작 정점 <em>R</em> (1 ≤ <em>R</em> ≤ <em>N</em>)이 주어진다.</p>

<p>다음 <em>M</em>개 줄에 간선 정보 <code><em>u</em> <em>v</em></code>가 주어지며 정점 <em>u</em>와 정점 <em>v</em>의 가중치 1인 양방향 간선을 나타낸다. (1 ≤ <em>u</em> < <em>v</em> ≤ <em>N</em>, <em>u</em> ≠ <em>v</em>) 모든 간선의 (<em>u</em>, <em>v</em>) 쌍의 값은 서로 다르다.</p>

### 출력 

 <p>첫째 줄부터 <em>N</em>개의 줄에 정수를 한 개씩 출력한다. <em>i</em>번째 줄에는 정점 <em>i</em>의 방문 순서를 출력한다. 시작 정점의 방문 순서는 1이다. 시작 정점에서 방문할 수 없는 경우 0을 출력한다.</p>

### 다른 코드 분석
> 이번 문제는 메모리와 시간 측면에서 부하가 큰 문제인 것 같다.
> 나는 딕셔너리에 노드와 방문순서를 저장하고 반복문으로 하나씩 호출했다.

[free0122님의 코드](https://www.acmicpc.net/source/52523362):
```python
cnt = 0
def solution():
    import sys
    sys.setrecursionlimit(10**6)

    N, M, R = map(int, sys.stdin.readline().split())   # 노드, 간선, 시작정점
    arr = [[] for i in range(N+1)]   # 0부터 N까지
    visited = [False] * (N+1)   # 하나 더 많은 False를 담은 리스트. 노드 번호와 인덱스를 맞추기 위함
    ans = ['0'] * (N)   # 출력할 실제 값이므로 N개

    # 그래프 그리기
    for i in sys.stdin.readlines():
        u, v = map(int, i.split())
        # 양방향 간선 그리기
        arr[u].append(v)
        arr[v].append(u)

    # 자식 노드들 오름차순 정렬
    for i in arr:
        i.sort()

    def dfs(x):
        global cnt   # global 키워드 용례
        cnt += 1
        visited[x] = True   # 방문처리
        ans[x-1] = str(cnt)
        for i in arr[x]:
            if visited[i] == False:
                dfs(i)

    dfs(R)
    print('\n'.join(ans))

solution()

```
> 메모리 약 74MB, 시간 508ms


[thesage님의 코드](https://www.acmicpc.net/source/43899345):
```python
from sys import*
setrecursionlimit(10**9)
M,R=lambda:map(int,stdin.readline().split()),range
def f(x):
 v[x]=c[0];c[0]+=1
 for e in g[x]:
  if v[e]<1:f(e)
n,m,r=M()
v=[0]*(n+1)
g=[[]for _ in R(n+1)]
for _ in R(m):a,b=M();g[a]+=[b];g[b]+=[a]
for i in R(n):g[i].sort()
c=[1]
f(r)
for e in v[1:]:print(e)

# Equivalently:
from sys import*
setrecursionlimit(10**9)

M, R = lambda: map(int, stdin.readline().split()), range
"""
>>> M
<function <lambda> at ... >   # lambda를 할당할 수도 있다.
>>> R
<class 'range'>
코드를 줄이기 위해 발휘한 창의력...
"""

c = [1]
def f(x: int) -> None:
    """
    각 노드(정수형)를 받으면 v[x]에 c[0]를 할당한다.
    c[0]을 1씩 증가한다.
    노드 x의 자식 노드들(e)을 순회하면서
    방문되지 않았으면 (v[e] < 1) 해당 노드에 대해 위 과정들을 반복한다(재귀).
    """
    v[x] = c[0]
    c[0] += 1
    for e in g[x]:
        if v[e] < 1:
            f(e)

n, m, r = M()
v = [0] * (n + 1)   # 출력될 리스트
g = [[] for _ in R(n + 1)]

# 그래프 그리기
for _ in R(m):
    # 양방향 간선
    a, b = M()
    g[a] += [b]
    g[b] += [a]

# 각 노드의 자식 노드들 정렬하기
for i in R(n):
    g[i].sort()

f(r)
for e in v[1:]:
    print(e)


```
> 메모리 약 159MB, 시간 732ms

1. 함수 내의 변수는 출력 되는 시점에 변수들이 선언되어 있으면 사용할 수 있는 것 같다.