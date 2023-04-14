# [unrated] 요격 시스템 - 181188 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181188) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.00 ms

# 코드 분석
## 내 코드 :
```python
import sys
from collections import deque
sys.setrecursionlimit(500_000)


def solution(targets):
    targets.sort()
    q = deque(targets)

    def f(q: deque, mark: int = 0, answer: int = 0) -> int:
        if not q:
            return answer
        e = mark
        while q:
            x, y = q.popleft()
            if x >= e:
                answer += 1
                e = y
            elif y <= e:
                return f(q, y, answer)
        return answer

    return f(q)
```
`[[1,2],[2,3],[3,4]]`와 같은 단순한 예에서 시작했다. 이전 구간의 마지막보다 시작이 앞서면 answer에 1씩 더하면 된다. 그런데 이런 접근에서 한가지 문제가 발상핸다. 바로 다음 구간이 이전 구간 위에 존재하는 경우다. 예를 들어 `[[0,4],[5,10],[6,8],[8,9]]`와 같은 경우에 3, 4번째 구간이 2번째 구간 위에 존재한다. 나는 이 문제를 3번째 구간 다음에 대해 재귀함으로 해결했다. `[0,4]`에서 answer에 1이 더해지고, `[5,10]`에서 다시 1이 더해지는데, 그 다음을 확인하니 시작점, 끝점도 이전 구간의 마지막보다 크지 않다. 이럴 경우 e를 y로 초기화해 재귀한다(`f(q, y, answer)`). `[5,10]`에서 answer가 이미 1 더해졌으니 재귀함수 안에서 새로운 e, mark보다 더 큰 값에 대해서만 answer를 더하면 된다. 이번 구간이 이전 구간 위에 있어 재귀했는데 그 다음 구간이 없거나, q가 소진되었을 때 answer를 리턴하고 종료한다.

<br>

## 이경준 님의 코드 :
```python
def solution(targets):
    answer = 1
    targets.sort()

    s,e = targets[0]
    for target in targets[1:]:
        if target[0] < e:
            if target[1] < e:
                e = target[1]
            continue
        else:
            s,e = target
            answer += 1

    return answer
```
이경준님은 같은 문제를 쉽게 해결했다. 현재 구간의 시작점과 끝점이 e보다 작으면 e를 현재 구간의 끝점으로 갱신한다. 그렇지 않을 때 또한 e를 갱신하는데 이때는 answer에 1을 더한다.

나는 시작점 때문에 기준점 효과를 겪었다고 볼 수 있다. 작은 구간들을 포함하는 더 큰 구간 대신, 작은 구간에 초점을 맞췄다면 좀 더 쉽게 풀었을지도 모른다~~고 생각하고 싶지만 이 또한 사후해석~~. 작은 구간에 쏘면 큰 구간은 저절로 맞추게 되니까.

<br>

