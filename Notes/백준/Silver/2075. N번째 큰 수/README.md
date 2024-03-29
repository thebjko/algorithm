# [Silver II] N번째 큰 수 - 2075 

[문제 링크](https://www.acmicpc.net/problem/2075) 


# 코드 분석

## [student_t 님의 코드 :](https://www.acmicpc.net/source/34312977)
```python
import sys

N = int(sys.stdin.readline().rstrip())
lst = []
for i in range((N // 2) - 1):
    lst.append(max(map(int, sys.stdin.readline().rstrip().split())))
for i in range((N // 2) - 1, N - 1):
    lst += sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)[:(N + 1) // (N - i) + 1]
lst += list(map(int, sys.stdin.readline().rstrip().split()))

lst.sort()
print(lst[-N])
```
> 메모리 약 30MB, 시간 692ms

1. `N // 2 - 1`번째 줄 까지는 최대값만 `lst`에 추가한다.
2. 그 이후 마지막줄 이전까지는 내림차순으로 정렬해 `(N+1)//(N-i)`번째 숫자까지만 추가한다.
3. 마지막 줄은 그대로 추가한다.

### 분석
#### 전체적인 그림
전체적으로 `lst`에 어떤 숫자들이 담기는지 봐야 한다. 각 줄(`sys.stdin.readline().rstrip().split()`)에는 `N`개의 숫자가 담겨있다. 마지막 줄은 `lst`에 모두 담지만, `(N//2)-1`번째 줄 부터 마지막 줄 이전까지는 `(N+1)//(N-i)`개 까지만 담는다. 리스트의 슬라이싱에는 인덱스에러가 나지 않는다. 그래서 `i`가 `N-2`일 때 원소가 `N`개인 줄을 인덱스 0부터 `N+1`까지 슬라이싱 하더라도 에러가 뜨지 않는다. 위로 올라갈수록 점점 `lst`에 담기는 숫자의 개수가 1/2, 1/3, 1/4... 의 비율로 줄어든다(inversely proportional). 상위 `N//2`개는 한개씩만 추가하면 된다. 전체적인 그림이 그려졌다. 왜 이래도 되는 것일까? 각 수는 자기 자신 바로 위의 수보다 크다라는 규칙이 있다. 그러면 위쪽 절반의 숫자들에 대해 각 줄의 최대값보다 큰 어떤 수가 다음 줄에 존재한다는 말이 된다. 

#### 2개 이상 존재하는 경우  
하지만 각 줄의 최대값보다 더 큰 수가 2개 이상 존재하는 줄이 생길 수 있다. 이대로 계속 진행한다면 N번째 큰 수가 누락될 수 있다. N번째 큰 수를 누락시키지 않기 위한 임계점은 어디인가? 어느 줄에 그 위 줄의 최대값보다 큰 수가 2개가 있다고 하자. 그 두 수 중 작은 수가 N번째 큰 수이고, 큰 수가 N-1번째 큰 숫자이다. 여기서 `max()`를 취해 `lst`에 추가한다면 N번째 큰 수가 누락되고 만다. 

만약 N번째 큰 수(`x`라 하자)가 k(k는 1 ~ `N//2-1`)번째 줄에 있다면 `lst`에 포함될 것이다. 만약 `x`가 그 줄에서 가장 큰 수(`y`라 하자)가 아니라면, `x`가 포함된 열 아래에 `x`보다 큰 수 `N-k`개가 존재하고, `y`가 포함된 열 아래로 `y`보다 큰 수 `N-k`개가 존재하게 된다. 따라서 `k`가 `N//2`가 되기 전 까지는 어떤 수 `x`가 N번째 큰 수이면서 그 줄에서 가장 큰 수가 아닐 수 없는 것이다. N이 짝수인 경우 N번째 큰 수를 제외하면 홀수개가 남으므로 `N//2-1`번째 줄 까지는 최대값을 취해도 괜찮다고 볼 수 있다.

예를 들어, 6개 줄인 경우 3번째 줄에 N번째 큰 수(`x`)가 있고, 3번째 줄의 가장 큰 수(`y`)는 아니라고 하자. `x` 아래로 `x`보다 더 큰수 3개가 있고, `y` 아래로 `y`보다 더 큰 수 3개가 있다. `y > x`이므로 `x`보다 더 큰 수는 6개가 존재하며, 따라서 `x`는 N번째 큰 수일 수 없다. 확인해보니 `N//2`까지 최대값을 취해도 통과되었다(676ms로 더 빨랐지만 약 31MB의 메모리를 소요했다). 

그 이후부터는 내림차순으로 정렬 된 리스트를 슬라이싱하는데, 위에서 도출된 원리에 따라 각 줄에 $가능한 개수 * 남은 줄 수 = N$가 되도록 슬라이싱한다.

### 잘 이해했는지 확인해보기
```python
import sys

input = sys.stdin.readline

N = int(input())

ls = []
for idx in range(N):
    ls += sorted(map(int, input().split()), reverse=True)[:N//(N-idx)]

print(sorted(ls)[-N])
```
> 메모리 약 31MB, 시간 788ms

이해한 바를 토대로 다시 만들어봤다. first half 줄을 정렬하느라 시간이 조금 소요되긴 했지만 원리를 제대로 적용했다. 마지막 줄과 first half는 정렬할 필요가 없어서 분리하면 성능을 좀 더 개선할 수 있을 것이다(student_t님의 코드처럼).

## [joonion 님의 코드 :](https://www.acmicpc.net/source/52615099)
```python
n = int(input())
a = []
for _ in [0] * n:
    a = sorted(a + [*map(int, input().split())])[-n:]

print(a[0])
```
> 메모리 약 31MB, 시간 936ms

매번 더하며 정렬해 N개를 추리는 코드.

## 내 코드
```python
import sys
from heapq import *

input = sys.stdin.readline
N = int(input())
heap = []
for _ in range(N):
    for i in map(int, input().split()):
        heappush(heap, i)
    
    while len(heap) > N:
        heappop(heap)

print(heappop(heap))
```
> 메모리: 33324 KB, 시간: 1700 ms

1. 그대로 구현했다. 메모리 부하를 최소화하기 위해 그때그때 `pop`을 하도록 했다.