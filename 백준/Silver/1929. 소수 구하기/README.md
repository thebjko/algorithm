# [Silver III] 소수 구하기 - 1929 

[문제 링크](https://www.acmicpc.net/problem/1929) 

### 성능 요약

메모리: 107712 KB, 시간: 5984 ms

### 분류

수학(math), 정수론(number_theory), 소수 판정(primality_test), 에라토스테네스의 체(sieve)

### 문제 설명

<p>M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.</p>

### 출력 

 <p>한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.</p>

### 다른 코드 분석
[rkddus96님의 코드](https://www.acmicpc.net/source/53387557):
```python
m, n = map(int, input().split())
li = [False] + [True] * ((n - 1) // 2)   # 뭐하는거지?
for x in range(1, int(n**.5/2+1)):   # 왜 제곱근을 2로 나누지? 소수의 비율과 관련있나?
  if li[x]:
    li[2*x*(x+1)::x*2+1] = [False] * ((((n + 1) // 2) - x * x * 2) // (x * 2 + 1))   # 리스트 한번에 바꾸기
if m <= 2:
  print(2)
print('\n'.join([f'{x}' for x, val in zip(range(m+(m&1==0), n+1, 2), li[m//2:]) if val]))

```
메모리 42.3MB, 시간 76ms로 엄청난 성능이다... 어떤 원리를 사용했을지 분석해보자.  

##### `range`를 제곱근을 2로 나눈 값에 관하여. 
내 코드에도 `if`문 조건을 `i > n ** .5/2+1`로 해도 1 1000000까지의 소수 개수가 정확히 나온다. 이 사실로부터 추측해볼 수 있는 것은, 이 코드도 순회할 리스트의 사이즈를 줄이는 방법을 사용하고 있다는 것이다 (feat. 에라토스테네스의 체).  

ChatGPT:  
> The reason why the division by 2 doesn't affect the proof is because dividing a number by 2 only changes its magnitude but not its relationship with other numbers. In this case, the relationship between the square root of n and the prime numbers in the range [1, n] is still the same regardless of whether the square root of n is divided by 2 or not. The proof still holds that all prime numbers in the range [1, n] will never be greater than the square root of n.

순회하는 숫자의 크기보다 관계에 의존하고 있기 때문이라고 한다.




cjfcjf님의 코드:
```python
m,n=map(int,input().split())
*l,=range(n+1)
for i in l[2:]:
 if l[i]>=m:print(i)
 l[i::i]=n//i*[0]

 ```
 메모리 약 84.6MB, 시간 608ms로 괜찮은 속도를 보인다.