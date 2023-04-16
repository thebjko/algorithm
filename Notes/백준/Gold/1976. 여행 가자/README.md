# [Gold IV] 여행 가자 - 1976 

[문제 링크](https://www.acmicpc.net/problem/1976) 

### 성능 요약

메모리: 31256 KB, 시간: 48 ms

### 분류

자료 구조, 그래프 이론, 그래프 탐색, 분리 집합

# 코드 분석
## 내 코드 :
```python
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

parent = [*range(N+1)]


def union(a: int, b: int):
    while a != parent[a]:
        parent[a] = parent[parent[a]]
        a = parent[a]
        
    while b != parent[b]:
        parent[b] = parent[parent[b]]
        b = parent[b]

    if a != b:
        if a > b:
            a, b = b, a
        parent[b] = a


for i in range(1, N+1):
    for j, k in enumerate(map(int, input().split()), 1):
        if k:
            union(i, j)

if len(set(parent[i] for i in map(int, input().split()))) > 1:
    print('NO')
else:
    print('YES')
```
1. 지난번에 배운 while문으로 find 함수를 대체하는 코드를 적용했다.
    - parent 테이블은 자기 자신으로 초기화되어있으므로 a가 `parent[a]`와 다르다면 상위 부모의 값을 끌어다가 같아질때까지 갱신하는 방법이다. 처음에는 그냥 통과하겠지만 아래에서 union을 하고 나서는 부모를 거슬러 올라가 같은 그룹에 속했던 모든 노드의 parent를 갱신하며 진행한다.
2. enumerate 함수에 두번째 인자는 인덱스의 시작점이다.
3. 세트 길이가 1보다 크면 연결되지 않은 그룹이 존재한다는 뜻.

## [jiyolla 님의 코드 :](https://www.acmicpc.net/source/25651160)
```python
import sys


def solve():
    read = sys.stdin.readline
    n, _ = int(read()), read()
    parent = [i for i in range(n)]

    def root(v):
        # 최종 parent를 리턴하지 않음
        while v != parent[v]:
            v = parent[v]
        return v
    for v1 in range(n):
        for v1_diff, connected in enumerate(read().split()[v1 + 1:]):
            v2 = v1 + v1_diff + 1
            if connected == '1':
                root_v1 = root(v1)
                root_v2 = root(v2)
                if root_v1 > root_v2:
                    parent[root_v1] = root_v2
                else:
                    parent[root_v2] = root_v1
                parent[v1] = parent[root_v1]
                parent[v2] = parent[root_v2]
    query = list(map(int, read().split()))
    ans = root(query[0] - 1)
    for i in query[1:]:
        if root(i - 1) != ans:
            ans = 'NO'
            break
    print(ans if ans == 'NO' else 'YES')


solve()
```
> 메모리 약 31MB, 시간 40ms

1. 자기 자신과는 연결되지 않았다고 친다. 그리고 양방향으로 연결되어있으므로 `[v1 + 1:]`으로 슬라이싱해 수행한다.
2. root 함수가 내 코드와 다른 방식으로 find를 구현한 것을 눈여겨보자. 