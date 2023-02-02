# [Bronze I] 가장 큰 금민수 - 1526 

[문제 링크](https://www.acmicpc.net/problem/1526) 

### 성능 요약

메모리: 31256 KB, 시간: 40 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation), 수학(math)

### 문제 설명

<p>은민이는 4와 7을 좋아하고, 나머지 숫자는 싫어한다. 금민수는 어떤 수가 4와 7로만 이루어진 수를 말한다.</p>

<p>N이 주어졌을 때, N보다 작거나 같은 금민수 중 가장 큰 것을 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 N이 주어진다. N은 4보다 크거나 같고 1,000,000보다 작거나 같은 자연수이다.</p>

### 출력 

 <p>첫째 줄에 N보다 작거나 같은 금민수 중 가장 큰 것을 출력한다.</p>

### 다른 코드 분석
[vkdidjvkdnj님의 코드](https://www.acmicpc.net/source/53476492):
```python
def solve(here):
    result = here
    if here * 10 + 4 <= N:
        result = max(result, solve(here * 10 + 4))
    if here * 10 + 7 <= N:
        result = max(result, solve(here * 10 + 7))
    return result

N = int(input())
print(solve(0))

```
> 메모리 약 30MB, 시간 36ms

<<<<<<< HEAD
4와 7에서 시작해 44, 47, 74, 77을 체크하는 코드. 재귀함수를 사용하는 방법을 보자.
=======
4와 7에서 시작해 44, 47, 74, 77, 444, 447, 474, 477, 744, ... 을 체크하는 코드. 재귀함수를 사용하는 방법을 보자.
>>>>>>> c8a6d97 (1526. 가장 큰 금민수 분석 완료)
