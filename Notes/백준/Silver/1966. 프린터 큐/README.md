# [Silver III] 프린터 큐 - 1966 

[문제 링크](https://www.acmicpc.net/problem/1966) 

# 코드 분석
## [puranium235 님의 코드 :](https://www.acmicpc.net/source/54316563)
```python
import sys

tc = int(sys.stdin.readline())

for _ in range(tc):
    n, wtk = map(int, sys.stdin.readline().split())
    li = list(map(int, sys.stdin.readline().split()))
    que = [(i, li[i]) for i in range(len(li))]
    li.sort(reverse=True)
    k = 0
    for el in li:
        while que[0][1] != el:
            tmp = que.pop(0)
            que.append(tmp)
        k += 1
        if que.pop(0)[0] == wtk:
            break
    print(k)
```
> 메모리 약 31 MB, 시간 36ms

1. 필요한 순간에만 간결하게 순서를 업데이트했다.
2. 인덱스와 값 잘 활용했다.

## [0cookieboy0 님의 코드 :](https://www.acmicpc.net/source/52788420)
```python
import sys
input = sys.stdin.readline

Q = []
R = []

for _ in range(int(input())):
    N, M = map(int, input().split())
    Q = list(map(int, input().split()))
    QS = sorted(Q, reverse=True)
    T = Q[M]
    Q[M] = -1
    result = 1

    while True:
        if Q[0] == -1 and max(QS) == T:
            R.append(result)
            break
        elif Q[0] == QS[0]:
            QS.pop(0)
            Q.pop(0)
            result += 1
        else:
            tmp = Q.pop(0)
            Q.append(tmp)

for r in R:
    print(r)
```
> 메모리 약 31 MB, 시간 36ms


## 내 코드
```python
import sys
from collections import deque

sys.stdin = open(0)
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    ls = deque(map(int, input().split()))

    radix = [0] * 10
    mark, num = 0, 0
    for idx, val in enumerate(ls):
        if idx == m:
            mark = radix[val]
            num = val
        radix[val] += 1
    
    order = 0
    k = 9
    while k > 0:
        while radix[k] and m >= 0:
            x = ls.popleft()
            if x == k:
                order += 1
                radix[k] -= 1
            else:
                ls.append(x)
            m -= 1
            if m < 0 and k != num:
                m = len(ls) - 1
        
        k -= 1

    print(order)
```
> 메모리: 34160 KB, 시간: 68 ms

1. 비교해보니 불필요한 점들이 많다. 왜 radix를 만든 것이며 불필요한 변수들이 많다. `num`이라던가 