# [Silver III] 구간 합 구하기 4 - 11659 

[문제 링크](https://www.acmicpc.net/problem/11659) 

### 성능 요약

메모리: 42340 KB, 시간: 236 ms

### 분류

누적 합

# 코드 분석
## [ljwljw8541 님의 코드 :](https://www.acmicpc.net/source/54336325)
```python
# https://www.acmicpc.net/source/54332769

from itertools import*
from sys import*
if __name__ == "__main__":
    Q=map(str.split, stdin.read().splitlines())
    next(Q)
    A = list(accumulate(map(int, next(Q)),initial=0))
    stdout.write('\n'.join(f'{A[int(b)]-A[int(a)-1]}'for a,b in Q))
```
> 메모리 약 48MB, 시간 136ms

눈여겨 볼 것들
1. next 함수 사용법
2. accumulate 함수의 initial 인자
3. stdin, stdout.write