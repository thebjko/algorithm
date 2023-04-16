# [unrated] 두 원 사이의 정수 쌍 - 181187 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181187) 

### 성능 요약

메모리: 10.4 MB, 시간: 1394.80 ms

# 코드 분석
## 내 코드 :
```python
def solution(r1, r2):
    answer = 0
    for a in range(-r2, r2+1):
        b = (r2**2-a**2)**.5
        answer += 2*int(b)+1

    for a in range(-r1, r1+1):
        b = (r1**2-a**2)**.5
        answer -= 2*int(b)+1
        if b - int(b) == 0:
            answer += 1 if b == 0 else 2

    return answer
```

<br>

## 조용운 님의 코드 :
```python
from math import sqrt

def solution(r1, r2):
    quar = 0
    for i in range(0, r1):
        quar += int(sqrt(r2**2 - i**2)) - int(sqrt(r1**2 - i**2 - 1))
    for i in range(r1, r2):
        quar += int(sqrt(r2**2 - i**2))
    return quar * 4
```
1. 1사분면을 두개의 구간으로 나눈다:
    1. 0부터 r1의 끝점 직전까지
    2. r1의 끝점부터 r2 직전까지
2. i를 증가시키며 높이를 구하고 정수 부분만 취해 차를 구한다. r1과 r2의 최소값은 1이므로 `sqrt(r1**2 - i**2 - 1)`에서도 에러가 나지 않는다. r1 위에 있는 점도 포함하기 때문에 -1을 한다.