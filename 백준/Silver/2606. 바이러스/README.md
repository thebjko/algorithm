# [Silver III] 바이러스 - 2606 

[문제 링크](https://www.acmicpc.net/problem/2606) 

### 성능 요약

메모리: 31256 KB, 시간: 40 ms

### 분류

그래프 이론(graphs), 그래프 탐색(graph_traversal), 너비 우선 탐색(bfs), 깊이 우선 탐색(dfs)

### 문제 설명

<p>신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.</p>

<p>예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.</p>

<p><img alt="" src="https://www.acmicpc.net/upload/images/zmMEZZ8ioN6rhCdHmcIT4a7.png" style="width: 239px; height: 157px; "></p>

<p>어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.</p>

### 출력 

 <p>1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.</p>

### 다른 코드 분석
[rossi22님의 코드](https://www.acmicpc.net/source/53099486):
```python
from sys import stdin

n = int(stdin.readline())
v = int(stdin.readline())

graph = [ [] for _ in range(n+1) ]
visited = [0] * (n+1)

for i in range(v) : 
    a, b = map(int, stdin.readline().split())

    graph[a] += [b]
    graph[b] += [a]

def dfs(k) : 
    visited[k] = 1

    for nx in graph[k] : 
        if visited[nx] == 0 : 
            dfs(nx)

dfs(1)
print(sum(visited)-1)
```
> 메모리 약 31MB, 시간 32m

어떤 점에서 빨랐을까?
1. 딕셔너리가 아니라 리스트를 사용했다. 단일인덱싱을 활용하니 시간복잡도는 O(1).
2. 재귀함수를 사용했다.
    - `dfs(1)`을 호출하면
    - `visited`리스트의 1번 인덱스가 1로 표시된다(방문표시).
    - 그리고 `graph`리스트의 1번 인덱스에 들어있는 리스트를 순회하면서
    - 방문하지 않은 곳에서 `dfs` 함수를 호출한다.
    - `visited`리스트에 방문된 곳은 1로 아닌 곳은 0으로 표시되어 있으니 합으로 출력.

[zzt님의 코드](https://www.acmicpc.net/source/20865270):
```python 
_,_,*i=open(0)
for _ in(n:=[-1,1]+[0]*99):
 for l in i:a,b=map(int,l.split());n[b]=n[a]=n[a]|n[b]
print(sum(n))

# Equivalently:
_, _, *i = open(0)
for _ in(n := [-1, 1] + [0] * 99):
    for l in i:
        a, b = map(int, l.split())
        n[b] = n[a] = n[a] | n[b]

print(sum(n))

```
> 메모리 약 29MB, 시간 80ms

1. 간선들만 받는다.
2. `n`을 99개의 0과 -1, 1을 갖는 리스트로 초기화한다(순서주의).
3. 간선 데이터를 순회한다.
    - 각 행으로 구분되어있다.
    - `a`, `b`에 정수형 값을 받아서 `n[b]`와 `n[a]`에 각각 두 값을 비트연산한 값을 넣는다.
    - 예를 들어
    - 1 2 라면 1이라는 값이 각각 들어간다.
    - 0과 1이 비트연산이 되면 1 1로 바뀐다. 0 0은 그대로 0 0, 1 1도 그대로 1 1.