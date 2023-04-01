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
_, *ls = map(int, open('input.txt').read().split())
for i in sorted(sorted(zip(ls[::2], ls[1::2]), key=itemgetter(0)), key=itemgetter(1)):
    print(*i)
```
> 메모리: 53144 KB, 시간: 284 ms