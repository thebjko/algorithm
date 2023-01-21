# [Bronze I] 부녀회장이 될테야 - 2775 

[문제 링크](https://www.acmicpc.net/problem/2775) 

### 성능 요약

메모리: 32540 KB, 시간: 40 ms

### 분류

다이나믹 프로그래밍(dp), 구현(implementation), 수학(math)

### 문제 설명

<p>평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어 각 층의 사람들을 불러 모아 반상회를 주최하려고 한다.</p>

<p>이 아파트에 거주를 하려면 조건이 있는데, “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 는 계약 조항을 꼭 지키고 들어와야 한다.</p>

<p>아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라. 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.</p>

### 입력 

 <p>첫 번째 줄에 Test case의 수 T가 주어진다. 그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다</p>

### 출력 

 <p>각각의 Test case에 대해서 해당 집에 거주민 수를 출력하라.</p>

### Note
뿌듯하다. 8전 9기.  
규칙을 발견해서 풀었다.  
아래는 다른 방법을 기록해둔다.
```python
# 재귀함수를 사용한 방법
_, *a = map(int, open("input.txt").read().split())

def num_inhabitants(k: int, n: int) -> int:    
    inhabitants = 0

    if k == 0:
        return n

    for i in range(1, n + 1):
        inhabitants += num_inhabitants(k - 1, i)
    
    return inhabitants

for i, j in zip(a[::2], a[1::2]):
    print(num_inhabitants(i, j))

```
정답 코드와 같은 값을 출력하지만 느려서 시간 초과가 뜬다.

### 숏코딩 분석
```python
# original:
import math
i=input
for n in[int]*int(i()):k=n(i());print(math.comb(k+n(i()),k+1))

# equivalent to:
import math

T = int(input())
for n in [int] * T:   # [int]는 뭐지?
    k = n(input())   # n이 이 줄의 input()값을 정수형으로 변환해준다.

    # comb 함수가 있었어.. factorial을 대신할 수 있었다.
    print(math.comb(k + n(input()), k + 1))   # 왜 comb(k + n, k + 1)인가?
    # factorial(k + n)/(factorial(k + 1)*factorial(n - 1))
    # 여기서 k + n 은 파스칼의 삼각형을 확장시켜서 n 차 더 올라가는 것이고
    # (예를 들어 4층 4호 -> 8차, 4층 1호 -> 5차)
    # k + 1 은 k + n 차의 이항계수에서 k + 1번째의 숫자를 선택하게 한다.
    # n - 1 이어도 된다. (식에서 볼 수 있듯) 같은 값을 준다.

```
