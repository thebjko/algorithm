# [Silver II] 스택 수열 - 1874 
> [문제 링크](https://www.acmicpc.net/problem/1874) 

## 코드 분석
### [ttasjwi 님의 코드 :](https://www.acmicpc.net/source/55591035)
```python
import sys


def solution():
    n, *nums = map(int, sys.stdin.buffer.read().splitlines())
    s = []
    answer = []
    cur = 1
    for value in nums:
        while cur <= value:
            answer.append('+')
            s.append(cur)
            cur += 1
        if s.pop() != value:
            return "NO"
        answer.append('-')
    return '\n'.join(answer)


print(solution())
```
> 메모리 약41MB, 시간 72ms

1. `sys.stdin.buffer.read()`를 통해 입력 시간을 아낀다.
2. 숫자 리스트를 순회하며
    1. `value`와 `cur`이 같아질 때까지 `cur`을 증가시키며 `s`에 추가한다.
    2. 같아졌을 때 답에 `-`를 추가한다. 하지만 만약 `s`의 마지막 값이 `value`와 다르다면 `NO`를 출력한다. 단순히 조회하는 것이 아니라 `pop()` 메서드로 제거한다. 
    3. 다음 값에 대해서도 같은 과정을 반복하는데, 
        1. 다음 값은 첫번째 값보다 크거나 작다. 
        2. 클 경우 `cur`을 계속 증가시킨다.
        3. 작을 경우 `s.pop()`을 실행하며 한번이라도 `value`와 다르다면 종료시킨다.
        4. 왜냐하면 한번이라도 다르다면 어차피 다음에 있을 그 값(`s.pop()` 된 값)이 `s`에 없을 것이기 때문이다.


### 내 코드
```python
n, *ls = map(int, open(0).read().split())
stack = [0]
result = ''

n = [*range(n, 0, -1)]
for i in ls:
    while stack[-1] < i:
        if not n:
            print('NO')
            exit()
        stack.append(n.pop())
        result += '+ '
    
    while stack[-1] > i:
        if stack[-1] == 0:
            print('NO')
            exit()
        stack.pop()
        result += '- '
    
    if stack[-1] == i:
        stack.pop()
        result += '- '
    
print(result)
```
> 메모리: 42172 KB, 시간: 2684 ms

요구사항을 구현했다. result의 공백 문자를 줄인다면 메모리를 더 아낄 수 있을까? 아래와 같이 수정하니 확실히 빨라졌다.

```python
n, *ls = map(int, open(0).read().split())
stack = [0]
result = []

k = 1
for i in ls:
    while stack[-1] < i:
        if k > n:
            print('NO')
            exit()
        stack.append(k)
        k += 1
        result.append('+')
    
    while stack[-1] > i:
        if stack[-1] == 0:
            print('NO')
            exit()
        stack.pop()
        result.append('-')
    
    if stack[-1] == i:
        stack.pop()
        result.append('-')
    
print(' '.join(result))
```
> 메모리 약 42MB, 시간 112ms

불필요한 리스트 사용을 줄이고, result에 공백문자를 줄였다.