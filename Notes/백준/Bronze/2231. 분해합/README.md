# [Bronze II] 분해합 - 2231 

[문제 링크](https://www.acmicpc.net/problem/2231) 

# 코드 분석
## [akkan 님의 코드 :](https://www.acmicpc.net/source/53246434)
```python
N = int(input())
ans = 0
for i in range(max(0,N-len(str(N))*9),N):
    if sum(map(int,str(i))) + i == N:
        ans = i
        break
print(ans)
```
> 메모리 약 31MB, 시간 32ms

역으로 갈 필요 없었다. 아래에서부터 조사해 하나가 나오는 순간 `break`로 탈출하면 됐다. 게다가 `ans`가 0에서 시작하니 조건문을 걸 필요도 없었다.

## 내 코드
```python
n = int(input())
result = int(1e6)
for i in range(n-1, max(n-9*len(str(n))-1, 0), -1):
    if i + sum(map(int, str(i))) == n:
        if i < result:
            result = i

print(result if result != int(1e6) else 0)
```
> 메모리: 31388 KB, 시간: 40 ms