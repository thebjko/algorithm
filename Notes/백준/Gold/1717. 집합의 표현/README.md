# [Gold V] 집합의 표현 - 1717 

[문제 링크](https://www.acmicpc.net/problem/1717) 

### 성능 요약

> 메모리: 83212 KB, 시간: 356 ms

### 분류

자료 구조, 분리 집합

# 코드 분석
## [hsh8086 님의 코드 :](https://www.acmicpc.net/source/55448622)
```python
import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
print = sys.stdout.write

def solve():   
    n, m = map(int, input().split())

    parent = list(range(n + 1))
    for _ in range(m):
        tp, a, b = map(int, input().split())
        
        while a != parent[a]:
            parent[a] = parent[parent[a]]
            a = parent[a]
            
        while b != parent[b]:
            parent[b] = parent[parent[b]]
            b = parent[b]

        if tp == 0:
            if a != b:
                if a > b:
                    a, b = b, a
                parent[b] = a
        else: print('YES\n') if a == b else print('NO\n')
            
if __name__ == '__main__':
    solve()
```
> 메모리 약 72MB, 시간 184ms

### 눈여겨 볼 점
1. 재귀함수가 아니라 반복문으로 `parent` 기록.
2. `union`을 조건문으로 처리.
    - `a`가 `b`보다 크다면 `parent[a]`에 `b`를 기록
    - 그렇지 않다면 `parent[b]`에 `a`를 기록
    - 여기서 `a`와 `b`는 각 주어진 값의 최상위 부모. 작은 쪽을, 큰 쪽의 테이블에 기록
3. [input과 print](https://velog.io/@thebjko/%EB%B0%B1%EC%A4%80-%EC%9D%B4%EB%B6%84-%EA%B7%B8%EB%9E%98%ED%94%84-%EC%BD%94%EB%93%9C-%EB%B6%84%EC%84%9D)
    - `io.BytesIO` : 메모리 바이트 버퍼를 열어 입력값을 받을 수 있게 한다.
    - `os.read` : 파일 기술자(첫번째 인자)에서 최대 두번째 인자만큼의 바이트를 읽는다. 0 은 `stdin`
    - `os.fstat(0).st_size` : `stdin`의 바이트 단위 파일 크기.

## 내 코드 :
```python
import sys
sys.setrecursionlimit(10**6)

i, *ls = open(0)

n, m = map(int, i.split())

parent = [*range(n+1)]

def find(x: int) -> int:
    if parent[x] != x:
        parent[x] = find(parent[x])   # 왜 이렇게?
    return parent[x]

def union(a: int, b: int):
    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for i in ls:
    if i[0] == '0':
        union(*map(int, i[2:].split()))
    else:
        a, b = map(int, i[2:].split())
        print('YNEOS'[find(a) != find(b)::2])   # 왜 이렇게 2
```
1. `find(x)`가 아니라 `find(parent[x])`
    - `find`는 부모를 찾는 함수이다. 최종 단계까지 올라가려면 부모의 부모를 찾는 재귀함수가 되어야 한다.
    - 예를 들어, (위 경우처럼 작은 쪽을 큰 쪽으로 합치는 경우)`parent[3]`에 4가 기록되어있다면, `parent[3]`에 `find(parent[4])`를 기록한다. 다음 단계에서 `parent[4]`에 5가 기록되어있으면 다시 `find(parent[4])`를 찾고, `parent[5]`에는 5가 기록되어있다고 하자. 결국 `find(3)`에서 `parent[3]`, `parent[4]`에 5가 기록된다.  
    하지만 반대로 `find(parent[x])` 대신 `find(x)`를 기록한다면, `parent[x]`가 자기자신이 아닌 경우, `parent[x]`에 `find(x)`, 즉, `parent[3]`이 3이 아니라면, 무한히 재귀하게 된다.
2. `parent[a] != parent[b]`가 아니라 `find(a) != find(b)`
    이 줄은 `a`와 `b`가 같은 집합에 속했다면 `YES`, 아니라면 `NO`를 출력하는 줄이다. 주의할 점은 아직 `parent` 테이블이 완전하지 않은 상태라는 것이다. 그래서 여기서 `parent` 테이블 대신 `find` 함수를 호출해 비교한다.