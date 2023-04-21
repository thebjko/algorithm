# [Silver II] 최소 힙 - 1927 

[문제 링크](https://www.acmicpc.net/problem/1927) 

### 성능 요약

메모리: 44020 KB, 시간: 120 ms

# 코드 분석
## [ttasjwi 님의 코드 :](https://www.acmicpc.net/source/55926137)
```python
import heapq
import sys

src = sys.stdin.buffer
print = sys.stdout.write

src.readline()
nums = list(map(int, src.read().splitlines()))

q = []
for num in nums:
    if num:
        heapq.heappush(q, num)
    else:
        if not q:
            print('0')
            print('\n')
        else:
            item = heapq.heappop(q)
            print(str(item))
            print('\n')
```
> 메모리 약 43MB, 시간 96ms

파이썬은 heapq 자료구조를 제공해줘서 문제 레벨 실버 2임에도 불구하고 쉽게 풀 수 있었다. node.js 같은 언어는 heapq를 구현해서 풀더라. 그리고 C 언어 같은 경우는 시간이 4ms로 엄청난 속도를 보였다.
1. `sys.stdin.buffer.read().splitlines()` : 버퍼에 모든 값을 불러와 줄 단위로 끊어 읽는다.
2. `sys.stdout.write` : 문자열을 출력한다.