# [Silver V] 좌표 정렬하기 2 - 11651 

[문제 링크](https://www.acmicpc.net/problem/11651) 

# 코드 분석
## [nansu0425 님의 코드 :](https://www.acmicpc.net/source/54468483)
```python
import sys

def cond(dot):
    x, y = dot.split()
    return int(y) + int(x)/1000000

dots = sorted(sys.stdin.readlines()[1:], key=lambda x: cond(x))
print(''.join(dots))
```
> 메모리 약 42MB, 시간 140ms

신박하다. `y`가 같으면 `x`로 정렬하는데, 두번째 줄부터 문자열로 받아 전처리 후 더한 값을 기준으로 정렬했다.

## 내 코드:
```python
from operator import itemgetter
_, *ls = map(int, open(0).read().split())
for i in sorted(sorted(zip(ls[::2], ls[1::2]), key=itemgetter(0)), key=itemgetter(1)):
    print(*i)
```
> 메모리: 53144 KB, 시간: 284 ms

## [sksk8922 님의 코드 :](https://www.acmicpc.net/source/53314897)
```python
import sys

coordinate = sys.stdin.readlines()[1:]
coordinate.sort(key=lambda x : int(x.split()[0]))
coordinate.sort(key=lambda y : int(y.split()[1]))
print("".join(coordinate))
```
> 메모리 약 42MB, 시간 172ms

로직은 같지만 내 코드는 `zip` 함수를 사용하는데서 아무래도 메모리 사용량이 더 컸나보다. `sorted`보다 `sort`가 'in-place'의 리스트를 사용하므로 메모리를 훨씬 덜 사용했을 것이다. 나는 리스트를 유지하면서도 `zip` 객체를 만들어야 했으니 메모리와 시간적인 측면에서 더 부하가 컸으리라 추측한다.