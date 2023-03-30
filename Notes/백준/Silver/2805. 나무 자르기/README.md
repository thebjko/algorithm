# [Silver II] 나무 자르기 - 2805 

[문제 링크](https://www.acmicpc.net/problem/2805) 

# 코드 분석
## 내 코드
```python
n, m, *ls = map(int, open(0).read().split())

def f(ls: list) -> int:
    min_ls = min(ls)
    max_ls = max(ls)
    n = len(ls)
    s = sum(ls)-n*min_ls

    if s <= m:
        return min_ls-(m-s+n-1)//n
    else:
        l,r = min_ls, max_ls
        while l <= r:
            mid = (l+r)//2
            ls_to_pass = []
            cut = 0
            for i, j in enumerate(ls):
                if j-mid > 0:
                    cut += j-mid
                    ls_to_pass.append(j)
            
            if cut > m:
                ls.clear()
                return f(ls_to_pass)
            else:
                r = mid-1


print(f(ls))
```
> 메모리: 149680 KB, 시간: 4448 ms

엄밀한 접근을 어떻게 해야 잘 할 수 있을까 고민하고 있었다. 특히 이분 탐색같은 경우 종료 조건과, 출력값이 이해가 잘 되지 않았다. 제일 먼저 생각해 본 것은, '가능한 케이스들을 어떻게 분류할 수 있을까'였다. 어떤 케이스들이 존재할까?  

크게 두 가지로 나눠보기로 했다. 최소값을 기준으로 잘랐을 때(`s = sum(ls)-n*min_ls`), `m`이 크거나 같은 경우와 그렇지 않은 경우. `s`가 `m`보다 작거나 같은 경우는 `n`개씩 늘려가면서 `s`가 `m`보다 커지는 바로 그 순간의 값을 반환하면 된다(`min_ls-(m-s+n-1)//n`). 그렇지 않은 경우에는 끝쪽 경계 `r`을 줄여가면서 탐색한다. `l`는 일반적인 이분 탐색에서 자른 나무들의 합이 `m`보다 작을 때 조정하는데, 이미 위에서 처리되었기 때문에 건드릴 필요가 없다. 다만 재귀할 때 최소값이 증가함에 따라 자연스럽게 올라가게 된다. 

양쪽 경계를 최소, 최대값으로 잡고 이분탐색을 진행한다. 재귀함수에 전달할 `ls_to_pass`를 초기화하고, `ls`를 순회하며 각 값에서 `l`과 `r`의 중간 `mid`를 뺀 값이 0보다 크면 자른 합 `cut`에 추가하고 `ls_to_pass`에 `append`한다. 같은 경우는 다음 단계에서 필요 없기 때문에 더 큰 값들만 추가하면 된다. 다음 재귀에서 `l`이 지금 단계의 `mid+1`이 된다고 생각하면 이해하기 쉽다. 그리고 자른 값 `cut`이 구하려는 값 `m`보다 크다면 `mid`보다 더 큰 값들에 대해 위 과정을 반복하면 된다. 메모리 관리를 위해 `ls.clear()` 메서드로 각 단계별 리스트를 비운다. `cut`이 `m`보다 작다면 `r`을 낮춘 뒤 다음 루프로 진행한다.

알고리즘 풀이 난이도가 올라감에 따라 점점 더 주먹구구식 접근과 시도가 늘어나고 있다. 엄밀한 접근법에 대해 배우려면 어디부터 손을 대야 하는걸까? 좋은 멘토가 있었으면 좋겠다.


## [parxism 님의 코드 :](https://www.acmicpc.net/source/54631551)

```python
import sys
from collections import Counter
n,m = map(int, sys.stdin.readline().split())
trees = Counter(map(int, sys.stdin.read().split()))

s = 1
e = 1000000000

while s<=e:
    mid = (s+e)//2
    tot = sum((h-mid)*i for h,i in trees.items() if h>mid)

    if tot >= m:
        s = mid+1
    elif tot <m:
        e = mid-1

print(e)
```
> 메모리 약 121MB, 시간 396ms

1. `Counter`를 사용해 자른 합을 구하는 시간을 줄였다.
2. 자른 합이 `m`보다 같거나 클 때 `s`를 늘이고 작을때 `e`를 줄였기 때문에 `e`를 출력했다.

이분 탐색의 교본으로 삼으면 되겠다.
