# [Silver II] 마인크래프트 - 18111 

[문제 링크](https://www.acmicpc.net/problem/18111) 

# 코드 분석
두 가지 작업이 가능하다: 인벤토리에 있는 블록을 쌓는 것과 쌓여 있는 블록을 인벤토리에 넣는 것. 언제부터 언제까지 어떤 작업을 수행해야 할지 어떻게 알 수 있을까? 만약 B가 0보다 크면, 작으면... 언제 덜어야되고 언제 더해야될지 어떻게 알 수 있을까 한참을 고민하다 반대로 생각해보기로 했다.

어떤 높이에서 평탄화 작업이 완료되었을 때, 이 경우가 가능한지 따져보도록 하자. 

## 내 코드 :
```python
from collections import Counter

_, _, B, *ls = map(int, open(0).read().split())


radix = Counter(ls)

def f(case: int, inventory: int, time: int = 0):
    for height, count in radix.items():
        x = count * abs(height - case)
        if not x:
            continue
        if height > case:
            inventory += x
            time += x*2
        elif height < case:
            inventory -= x
            time += x

    if inventory < 0:
        return float('inf')
    
    return time


time, c = float('inf'), 0
for tc in range(min(radix), max(radix)+1):
    t = f(tc, B)
    if t <= time:
        time = t
        c = tc

print(time, c)
```
> 메모리: 51708 KB, 시간: 172 ms

사실 입력값이 2차원 매트릭스라는 사실은 이 구현에서 크게 중요하지 않았기 때문에 1차원 리스트로 받았다. 각 값의 빈도를 `Counter` 클래스를 사용해 `radix`에 기록했다. 가장 낮은 높이에서 더 덜 필요가 없고, 가장 높은 높이에서 더할 필요가 없기 때문에 가능한 케이스의 범위는 최소값에서 최대값으로 잡았다. 각 케이스에 대해 함수 `f`를 실행해 `time`에 기록된 값보다 더 작은 값이 반환될 때마다 걸린 시간 `t`와 높이 `tc`를 기록한다.

이제 함수를 살펴보자. 케이스의 범위에 속한 정수와 인벤토리에 있는 블록의 개수, 그리고 시간을 기록할 변수를 받는다. 시간을 기록할 변수는 안에서 초기화해도 상관없다. 현재 높이 `case`보다 낮은 값에 인벤토리에서 블록을 가져와 채우고, 하나당 1초씩 기록한다. 더 높은 값에서 블록을 덜어 인벤토리에 채우며 하나당 2초씩 기록한다. `Counter`를 사용해 각 높이당 한번에 계산한다. 그렇게 평탄화 작업을 진행했을 때, 인벤토리가 음수라면 이 케이스는 불가능한 케이스이므로 `float('inf')`를 반환, 그렇지 않다면 걸린 시간을 반환한다.

### 수정사항 반영한 코드
```python
from collections import Counter

_, _, B, *ls = map(int, open(0).read().split())


radix = Counter(ls)

def f(case: int):
    inventory, time = B, 0
    for height, count in radix.items():
        if height == case:
            continue
        x = count * abs(height - case)
        if height > case:
            inventory += x
            time += x*2
        elif height < case:
            inventory -= x
            time += x

    if inventory < 0:
        return float('inf')
    
    return time


time, c = float('inf'), 0
for tc in range(min(radix), max(radix)+1):
    t = f(tc)
    if t <= time:
        time = t
        c = tc

print(time, c)
```
> 메모리: 52112 KB, 시간: 148 ms

수정 이전보다 메모리를 약간 더 사용하면서 약간 빨라졌다.

함수 안에서 `abs` 함수를 제거하면, 메모리  51708 KB, 시간 136 ms까지 개선할 수 있다.

```python
        if height == case:
            continue
        if height > case:
            x = count * (height-case)
            inventory += x
            time += x*2
        elif height < case:
            x = count * (case-height)
            inventory -= x
            time += x
```


## [lambda 님의 코드 :](https://www.acmicpc.net/source/53151841)
```python
import sys


input = sys.stdin.readline

def sol():
    n, m, b = map(int,input().split())
    data = [0]*257
    for _ in range(n):
        for i in map(int,input().split()):
            data[i] += 1
    have = sum(i*data[i] for i in range(257))   # 쌓여있는 블록 개수
    need = 0
    t = data[0]   # 높이가 0인 구역의 개수
    nm = n*m
    for i in range(1, 257):   # i는 높이
        need += t   # 현재 높이보다 낮은 구역의 개수를 더한다. 현재 높이 i로 맞추기 위해 필요한 블록의 개수.
                    # 누적합이다. 좀 더 정확히 말하면 높이가 0인 구역의 개수는 i가 올라감에 따라 하나씩 계속 더해지고 있다.
                    # 높이가 1인 구역의 개수는 i가 2부터 올라감에 따라 하나씩 계속 더해지고 있다.
                    # 2인 구역인 개수는 3부터, 3인 구역인 개수는 4부터.
                    # 즉, i가 1일 때, 높이가 1로 평탄화 작업이 되는 경우 높이가 0인 구역에 하나씩 쌓는다는 말.

        have -= nm-t   # 전체 구역 개수에서 현재 높이보다 낮은 구역의 개수를 뺀 값(현재 높이보다 같거나 높은 값)을 have에서 제한다
                       # 현재 높이보다 같거나 높은 값을 쌓여있는 블록 개수에서 제한다.
                       
        t += data[i]   # 높이가 0~i인 구역의 개수 t
        if have+b-need < 0:   # 적자가 나면 종료
            break             # need는 계속 커질 것이기 때문에 계속 진행하는게 의미가 없음. continue(X) -> break
        else:
            ans = min((have*2+need, -i), ans)
    
    print(ans[0], -ans[1])

sol()
```
> 메모리 약 31MB, 시간 88ms

1. radix를 활용(`data`)
2. 튜플에 `min` 함수를 사용해 시간이 더 적은 케이스를 선택하도록 했고, 시간이 같다면 높이가 더 높은 케이스를 선택하도록 했다(`-i`).
3. 주석으로 기록했다.