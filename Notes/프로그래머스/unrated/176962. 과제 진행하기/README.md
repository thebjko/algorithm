# [unrated] 과제 진행하기 - 176962 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/176962) 

### 성능 요약

메모리: 10.6 MB, 시간: 23.61 ms

# 코드 분석
## 김남준, JooJaeHwan 님의 코드
```python
def solution(plans):
    plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: -x[1])

    lst = []
    while plans:
        x = plans.pop()
        for i, v in enumerate(lst):
            if v[0] > x[1]:
                lst[i][0] += x[2]
        lst.append([x[1] + x[2], x[0]])
    lst.sort()

    return list(map(lambda x: x[1], lst))

```
1. 시작 시간의 역순으로 정렬(숫자일때는 부호 변환한 수를 키로 사용해 정렬)
2. 끝나는 시작으로 `lst`에 append한다. 
    - 각 plan이 시작하는 시간보다 끝나는 시점이 늦다면, 이전 plan의 끝나는 시간에 이번 plan의 duration을 더한다.
    - `lst`를 순회하며 해당하는 plan의 끝나는 시점을 모두 늦춘다.
3. 정렬하여 반환한다.

<br>

## 내 코드
```python
from operator import itemgetter as ig


def timer(time: str) -> int:
    h, m = map(int, time.split(':'))
    return h * 60 + m


def solution(plans):
    answer, stack = [], []
    for plan in plans:
        plan[1], plan[2] = timer(plan[1]), int(plan[2])
    
    plans.sort(key=lambda ls: ls[1])
    
    t, idx = plans[0][1], 0
    while idx < len(plans):
        stack.append(plans[idx])
        if t < stack[-1][1]:
            t = stack[-1][1]

        while stack and stack[-1][2]:
            t += 1
            stack[-1][2] -= 1
            if not stack[-1][2]:
                answer.append(stack.pop())
            if idx+1 < len(plans) and t == plans[idx+1][1]:
                stack.append(plans[idx+1])
                idx += 1
        idx += 1
        
    return list(map(ig(0), answer))


if __name__ == '__main__':
    test_cases = [
        [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]],
        [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]],
        # bbb, aaa, ccc
        [["aaa", "12:00", "30"], ["bbb", "12:10", "30"], ["ccc", "14:00", "30"]],
        [['A', "12:00", "30"], ['B', "12:10", "20"], ['C', "15:00", "40"], ['D', "15:10", "30"]],
    ]
    for tc in test_cases:
        print(solution(tc))

```
