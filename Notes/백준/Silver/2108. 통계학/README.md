# [Silver III] 통계학 - 2108 

[문제 링크](https://www.acmicpc.net/problem/2108) 

# 코드 분석
## [cjfcjf 님의 코드 :](https://www.acmicpc.net/source/39729431)
```python
import collections as c
n, *l = map(int, open(0))
l.sort()
t = c.Counter(l).most_common(2)
print(round(sum(l)/n), l[n//2], t[-(t[0][1]==t[-1][1])][0], l[-1]-l[0])
```
> 메모리 약 53 MB, 시간 376 ms

최빈값을 구하는 부분을 눈여겨보자. 

0. `Counter` 클래스의 `most_common()` 메서드는 [최빈값을 구해 최빈값과 빈도수 튜플을 담은 리스트로 반환](https://docs.python.org/3/library/collections.html#collections.Counter.most_common)한다. 
1. 최빈값을 2개까지 구하는데, sort할 필요는 없나보다. `l`이 정렬되어있기 때문이다. `Counter` 클래스는 빈도수를 따라 내림차순으로 정렬하고, 키로는 정렬하지 않고 반환한다.
2. `t`의 첫 번째 튜플과 두번째 튜플의 빈도가 같다면 두 번째 튜플, 같지 않다면 첫 번째 튜플의 최빈값을 출력한다.

## [dragonldh 님의 코드 :](https://www.acmicpc.net/source/37033270)
```python
from sys import stdin


def sol2108():
    n = int(stdin.readline())
    counts = [0]*8001   # 기수 정렬
    s = 0
    for i in stdin:
        num = int(i)
        counts[num+4000] += 1

    maxc = max(counts)   # 최빈값
    mode = mcnt = 0
    idx = 0
    med = None
    mi, ma = 4001, -4001
    for i in range(8001):
        cnt = counts[i]
        if cnt == 0:
            continue

        num = i-4000   # i를 실제 값으로 조정
        s += num*counts[i]   # 전체 합계를 구하기 위함(sum)
        if cnt == maxc and mcnt < 2:
            mode = num   # 최빈값 기록
            mcnt += 1    # 최빈값 개수 2개까지만 기록
        mi = min(mi, num)
        ma = max(ma, num)
        idx += counts[i]
        if idx >= n//2+1 and med == None:
            med = num   # 중간값 기록. 
                        # -4000부터 4000까지 개수를 세다가
                        # 전체 개수의 가운데를 넘어간다면 기록
                        # (n은 홀수)
    print(round(s/n), med, mode, ma-mi, sep='\n')


if __name__ == '__main__':
    sol2108()
```
> 메모리 약 31 MB, 시간 176 ms

이런 성능을 지나칠 수 없다. 성능 차이가 어디서 오는걸까?

1. `stdin` 사용. 전체 수를 담는 리스트 대신 기수 정렬을 사용해 메모리 사용을 줄였다.
2. 따라서 전체 리스트에 대해 `sum`, `min`, `max`를 사용하지 않고 최대, 최솟값을 매번 갱신하는 방식으로 구했다. (`s += num*counts[i]`, `mi = min(mi, num)`, `ma = max(ma, num)`)

일단 전체 리스트를 다 메모리에 올리지 않는 방식으로 시작해, 어떻게 할지 고민해 구현한 것이다.


## 내 코드
```python 
from collections import Counter
n, *ls = map(int, open('input.txt').read().split())
ls, counter = sorted(ls), Counter(ls)
most_common = counter.most_common(1)[0][1]
filtered = sorted(filter(lambda x: counter[x] == most_common, counter))

print(round(sum(ls)/n), ls[n//2], filtered[len(filtered)>1], ls[-1]-ls[0])
```
> 메모리: 90024 KB, 시간: 376 ms

최빈값이 여러개 있을 때 2번째로 작은 수를 어떻게 구할까 고민하다가 위와 같이 작성했다. 논리는 cjfcjf님의 코드와 비슷한 것 같다. 메모리 비효율이 어디서 발생했나?

1. 입력 값을 `.read().split()`할 필요가 없었다.
2. 리스트와 카운터를 다 저장해 cjfcjf님의 코드와 메모리가 최악의 경우 2배가량 차이날 수 밖에 없었다.