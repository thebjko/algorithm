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
# 1은 소수가 아니므로 False, 나머지는 True라고 가정하여 시작
# 2의 배수는 제거한 개수만큼 True 추가 ((n - 1) // 2) 
li = [False] + [True] * ((n - 1) // 2)   
# 초기 리스트의 개수를 n의 반으로 줄였으므로 n**.5 나누기 2를 해도 된다.
for x in range(1, int(n ** .5 / 2 + 1)):   
  print(li, len(li))
  if li[x]:   # li[1] == 2는 True
    # 뭐하는거지..?
    # 일단 1의 배수들을 제외한 각 수의 배수들에 해당하는 인덱스를 True에서 False로 바꾸는 작업일 것이다.
    # li에 해당하는 숫자는 1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, ..., 99
    # x가 1일 때 li[4::3]는 1, 2, 3, 5를 건너뛰어서 7부터 3씩 ->  7, 13, 19, ... ??
    # 그 개수만큼 False라면 왜 len()함수를 사용하지 않았나
    # 아마 시간복잡도 때문일 것 같다. 순회보다 계산이 빠르니까
    # n = 100, x = 1 이라 하면 (50 - 2) // 3 == 16개의 False
    # 왜 7부터이지?
    # 9 부터여야 하는거 아닌가?
    # 설마 첫번째 False가 2를 가리키고 있는건가? 그러면 n = 100일때 len(li) == 50으로 딱 말이 된다.
    # 아래에서 if m <= 2: print(2) 도 말이 된다
    # 아니다 아마 1 3 5 7... 일 것이다. 그래서 밑에서 2를 따로 print 해주는 것일 것이다
    # 그렇다면 말이 된다. li에 해당하는 숫자가 1,3,5,7,9, ... 이고
    # x가 1일 때 li[4::3]은 9부터 3씩 False
    # x가 2일 때 li[12::5]는 25부터 5씩.. 와우..
    # 2*x*(x+1): 4, 12, 24, 40, 60, 84, 112, 144, 180, 220, ... (x**2)+x+2
    # 해당하는 수는 3, 5, 7, 9, 11, 13, ... 의 제곱수
    # x*2+1: 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, ...   2씩 증가
    # 3의 제곱수에서부터 3씩, 5의 제곱수에서부터 5씩, 7의 제곱수에서부터 7씩 증가
    """
    그도 그럴것이 3의 배수 찾았으면 5의 배수, 7의 배수, 9의 배수 찾아서 제거하면 되고.
    li가 홀수를 가리키고 있고,
    x가 1부터라면
    3의 배수 중 3을 제외한 9부터 시작해서 3배수를 False처리
    5의 배수 중 5를 제외한 25부터 시작해서 5의 배수를 False처리 ... 하려면
    1 -> 9(를 가리키는 인덱스 4) -> 3씩 증가
    2 -> 25(를 가리키는 인덱스 12) -> 5씩 증가
    3 -> 49(를 가리키는 인덱스 40) -> 7씩 증가
    4 -> 81(를 가리키는 인덱스 60) -> 9씩 증가 (이미 False이므로 if li[x]에서 건너뛸 것 -> 순회 최소화)
    ...
    매핑이 되게 하려면 적절한 규칙을 찾아서 리스트의 시작점에 꽂아주고
    x가 1일 때 3, 2일때 5 ... 등등이 되도록 해서 슬라이싱되도록 꽂아주면 된다
    
    위에서 언급했듯 len함수는 시간복잡도가 O(N)이다.
    그런데 n과 x가 주어졌을 때 계산해낼 수 있다면 시간복잡도가 훨씬 줄어들 수 있을 것이다.
    그것을 계산한 부분이 바로 ((((n + 1) // 2) - x * x * 2) // (x * 2 + 1)) 이 부분
    위에서 리스트의 크기를 1 + ((n - 1) // 2)개수로 했다면 일단 ((n + 1) // 2)로 전체크기를 잡고
    (n == 100일 때 50)
    리스트가 2*x*(x+1)에서 시작하니 (2 * (x ** 2) + (2 * x)) 
    (x == 1일 때 4, 슬라이스 된 li의 크기는 46이므로)
    50에 2를 뺀 수 48를 3으로 나눈 몫을 구하면(3씩 증가하므로)
    16개의 False를 원소로 갖는 리스트가 만들어진다.    

    """
    li[2*x*(x+1)::x*2+1] = [False] * ((((n + 1) // 2) - x * x * 2) // (x * 2 + 1))
if m <= 2:
  print(2)
# "&"는 비트 단위의 AND 연산자 - 동일한 위치의 bit가 1인 것들만 1로 계산. 결국 "& 1" 은 "% 2"와 같다
# https://codechacha.com/ko/python-difference-and-ampersand/
# 3부터 출력한다.
print(' '.join([f'{x}' for x, val in zip(range(m+(m&1==0), n+1, 2), li[m//2:]) if val]))

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