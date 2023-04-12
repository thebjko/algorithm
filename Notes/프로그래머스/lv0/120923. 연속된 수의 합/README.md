# [level 0] 연속된 수의 합 - 120923 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120923) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.01 ms

# 코드 분석
DalHyun , 조현 , 포메 , 안형우 외 2 명:
```python
def solution(num, total):
    return [(total - (num * (num - 1) // 2)) // num + i for i in range(num)]
```
1. `total` : `(x+0) + (x+1) + (x+2) + ... + (x+num-1)`
2. `total`에서 1부터 `num-1`까지 더한 값을 빼면 `x*num`이 된다(`x`가 `num`개 있는 배열의 합).
3. 각 값에 0, 1, ... , num-1을 다시 더하면(`+ i for i in range(num)`) 답을 구할 수 있다.