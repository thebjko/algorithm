# [Gold IV] 플로이드 - 11404 

[문제 링크](https://www.acmicpc.net/problem/11404) 

### 성능 요약

> 메모리: 40304 KB, 시간: 608 ms

# 코드 분석
## [silence1230 님의 코드 :](https://www.acmicpc.net/source/55414335)
```python
import sys
input = sys.stdin.readline

def sol(n: int, m: int) -> str:
    INF = sys.maxsize

    time_table = [[INF]*n for _ in range(n)]
    for i in range(n):
        time_table[i][i] = 0
    for _ in range(m):
        a,b,c = map(int, input().split())
        if c < time_table[a-1][b-1]:
            time_table[a-1][b-1] = c

    for i in range(n):
        for j in range(n):
            if i==j or time_table[j][i]==INF:
                continue
            for k in range(n):
                if i==k:
                    continue
                if time_table[j][i]+time_table[i][k] < time_table[j][k]:
                    time_table[j][k] = time_table[j][i]+time_table[i][k]

    return '\n'.join(' '.join('0' if d==INF else str(d) for d in line) for line in time_table)


print(sol(int(input()), int(input())))
```
> 메모리 약 31 MB, 시간 220 ms

성능 차이가 어디서 발생한걸까? 로직에서 크게 다르지 않은 것 같은데. 현재로써는 `min()` 함수를 쓴 데서 차이가 왔다고밖에 볼 수 없다.


## 기존 코드
```python
from math import inf, isinf

n, m, *ls = open(0)
n = int(n)
m = int(m)


matrix = [[inf] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    matrix[i][i] = 0

for i in ls:
    a, b, c = map(int, i.split())
    matrix[a][b] = min(matrix[a][b], c)


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            matrix[a][b] = min(matrix[a][b], matrix[a][k] + matrix[k][b])


for i in matrix[1:]:
    for val in i[1:]:
        print(0 if isinf(val) else val)
```
> 메모리 약 40 MB, 시간 608 ms

## 수정한 코드
```python
from math import inf, isinf

n, m, *ls = open(0)
n = int(n)
m = int(m)


matrix = [[inf] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    matrix[i][i] = 0

for i in ls:
    a, b, c = map(int, i.split())
    if c < matrix[a][b]:
        matrix[a][b] = c


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if matrix[a][b] > matrix[a][k] + matrix[k][b]:
                matrix[a][b] = matrix[a][k] + matrix[k][b]

print('\n'.join(' '.join('0' if isinf(val) else str(val) for val in i[1:]) for i in matrix[1:]))
```
> 메모리 약 40 MB, 시간 408 ms

확실히 시간이 줄어들었으나 여전히 멀었다. INF와 입력방식의 차이를 살펴보자 inf를 `sys.maxsize`로 고치니 시간이 400ms로 아주 약간 줄었고 `input = sys.stdin` 사용시 392ms로 아주 미미한 차이밖에 없었다. 둘 다 적용해도 372ms까지밖에 안 줄었다.