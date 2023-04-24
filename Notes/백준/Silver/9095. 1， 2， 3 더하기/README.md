# [Silver III] 1, 2, 3 더하기 - 9095 

[문제 링크](https://www.acmicpc.net/problem/9095) 

### 성능 요약

메모리: 31256 KB, 시간: 44 ms

# 코드 분석
## [kdi1569 님의 코드 :](https://www.acmicpc.net/source/52744356)
```python
T = int(input())
a = [int(input()) for _ in range(T)]
c = [0]*(11)
c[1] = 1
c[2] = 2
c[3] = 4
for i in range(4, 11):
    c[i] = c[i-1] + c[i-2] + c[i-3]
for b in a:
    print(c[b])
```
> 메모리 약 31MB, 시간 32ms

## 내 코드 :
```python
_, *ls = map(int, open(0).read().split())

def dfs(x: int):
    stack = [1, 2, 3]
    answer = 0
    while stack:
        u = stack.pop()
        if u == x:
            answer += 1
        for i in (1, 2, 3):
            v = u + i
            if v > x:
                continue
            stack.append(v)

    return answer

for i in ls:
    print(dfs(i))
```
