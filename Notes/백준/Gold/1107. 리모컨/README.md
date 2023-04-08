# [Gold V] 리모컨 - 1107 

[문제 링크](https://www.acmicpc.net/problem/1107) 

### 성능 요약

메모리: 136808 KB, 시간: 1500 ms

### 분류

브루트포스 알고리즘

# 코드 분석
## [pank0415 님의 코드 :](https://www.acmicpc.net/source/54756862)
```python
import sys


def get_score(candidate: int):
    '''자리수(버튼 누르는 횟수) + 후보에서 N까지 이동하는데 필요한 +,- 버튼 누르는 횟수'''
    digits_count = len(str(candidate))
    return digits_count + abs(N - candidate)


def dfs(cur_filled_digits: int, acc_number: int):
    candidates = []
    filled_num = cur_filled_digits
    if filled_num == digits_length:
        return acc_number
    zeros = digits_length - filled_num - 1
    multiple_value = 10 ** zeros
    target = digits[filled_num]
    closest_big = next((x for x in usable_buttons if x > target), None)
    closest_small = next((x for x in rev_usable_buttons if x < target), None)

    if closest_big is not None:
        bigger_num = acc_number + int(str(closest_big) + str(least_button) * zeros)
        candidates.append(bigger_num)
    else:
        if filled_num == 0:
            if least_nonzero != -1:
                bigger_num = int(str(least_nonzero) + str(least_button) * (zeros + 1))
                candidates.append(bigger_num)
    if closest_small is not None:
        smaller_num = acc_number + int(str(closest_small) + str(last_button) * zeros)
        candidates.append(smaller_num)
    else:
        if filled_num == 0:
            if last_button != 0 and zeros != 0:
                smaller_num = int(str(last_button) * zeros)
                candidates.append(smaller_num)

    if target in usable_buttons:
        candidates.append(dfs(filled_num + 1, acc_number + multiple_value * target))

    if len(candidates) == 0:
        return 0
    else:
        scores = list(map(get_score, candidates))
        i = scores.index(min(scores))
        return candidates[i]


def get_closest_number():
    use_digits_button_case = dfs(0, 0)
    make_use_of_start_case = abs(100 - N)

    return min(get_score(use_digits_button_case), make_use_of_start_case)


N = int(input())
mal_cnt = int(input())
if mal_cnt > 0:
    mal_buttons = list(map(int, sys.stdin.readline().split()))
else:
    mal_buttons = []
digits = list(map(int, list(str(N))))
digits_length = len(digits)


usable_buttons = list(range(10))
for mal_button in mal_buttons:
    usable_buttons.remove(mal_button)

if len(usable_buttons) == 0:
    print(abs(100 - N))
else:
    usable_buttons.sort()
    rev_usable_buttons = list(reversed(usable_buttons))
    least_button, last_button = usable_buttons[0], usable_buttons[-1]
    if least_button == 0:
        if len(usable_buttons) > 1:
            least_nonzero = usable_buttons[1]
        else:
            least_nonzero = -1
    else:
        least_nonzero = least_button

    print(get_closest_number())
```
> 메모리 약 31MB, 시간 36ms

제출하고 답이 체크되는 동안 이런 성능은 어떻게 나올 수 있는지 정말 궁금해졌다.

## 내 코드 :
```python
from heapq import *

N, M, *ls = map(int, open(0).read().split())
s = set(str(i) for i in ls)

if N == 100:
    print(0)
    exit()

if M == 10:
    print(abs(N-100))
    exit()



heap = [(0, N)]
for i in range(0, 10**6):
    str_i = str(i)
    for j in str_i:
        if j in s:
            break
    else:
        heappush(heap, (min(abs(i-100), len(str_i)), abs(N-i)+100))

while heap:
    cost, cur = heappop(heap)
    if cur == 100:
        print(cost)
        break
    heappush(heap, (cost + abs(cur-100), 100))
```
0. 범위에 대해
500_000으로 이동하려고 하는데 가능한 버튼이 9밖에 없다면 99_999에서 +를 눌러 이동하는게 999_999에서 내려오는것보다 빠르다. 하지만 8만 가능하다면, 88_888에서 올라가는 것보다 888_888에서 내려오는게 더 빠르다. 8과 9가 가능하더라도 여전히 888_888에서 내려오는게 더 빠르다. 그렇다면 각 수에 대해 어디가 상한선일까? 이를 계산하는 비용을 치르는 대신 999_999까지 확인하기로 한다.
1. 범위 안의 각 수에 대해 사용 가능한 버튼으로 구성되어있다면
    1. 그 수로 이동하는 비용 중 더 적은 비용과, 그 수와, 가고자하는 수의 차이에 100을 더한 값을 heappush한다.
        - 101은 길이가 3이지만 +버튼 한번으로 갈 수 있다.
        - 그 지점부터 목표지점 N까지는 플러스버튼을 눌러서 간다(`abs(N-i)`) +, - 버튼을 한번 누를때마다 100을 1씩 증감하는 대신, N을 감소/증가한다.
        - 100이 종료지점이 되기 때문에 100을 더한다. 이렇게 하지 않으면 종료지점에 도달하지 않았음에도(ex. N=400, i=300) 아래 while문에서 종료되어버린다.
2. 그렇게 추린 수들 중 가장 비용이 적은 채널을 확인한다.
    - 현재 채널과 +, -버튼을 눌러 갈 목표지점 N의 차이를 cost에 더하고, 종료조건인 100과 함께 heappush.
    - 비용이 가장 적은 방법이 가장 먼저 종료지점에 도달할 것이다. 비용을 출력하고 break.
    - 


# 반례모음
1. https://www.acmicpc.net/board/view/46120
2. https://www.acmicpc.net/board/view/69884
3. https://www.acmicpc.net/board/view/107529
4. https://www.acmicpc.net/board/view/31853
