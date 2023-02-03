# [Silver III] 소수 구하기 - 1929 

[문제 링크](https://www.acmicpc.net/problem/1929) 

### 성능 요약

메모리: 59276 KB, 시간: 104 ms

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

아래와 같이 좀 더 직관적으로 수정했다. 자세한 내용은 [velog글](https://velog.io/@thebjko/%EB%B0%B1%EC%A4%80-1929.-%EC%86%8C%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0-%EC%BD%94%EB%93%9C-%EB%B6%84%EC%84%9D) 참조:
```python
from math import ceil

m, n = map(int, input().split()) 
ls = [0, *range(3, n+1, 2)]

for x in range(1, int(n**.5/2+1)):
    if ls[x]:
        ls[2*x*(x+1)::x*2+1]=[0]*ceil(((((n+1)//2)-x*x*2-x*2)/(x*2+1)))
        
if m <= 2:
    print(2)

print(' '.join([f'{val}' for val in ls[m//2:] if val]))
```

[cjfcjf님의 코드](https://www.acmicpc.net/source/39443229):
```python
m,n=map(int,input().split())
*l,=range(n+1)
for i in l[2:]:
 if l[i]>=m:print(i)
 l[i::i]=n//i*[0]

# Equivalently:
m, n = map(int, input().split())
*l, = range(n + 1)
for i in l[2:]:
    if l[i] >= m:
        print(i)
    l[i::i] = n // i * [0]

```
> 메모리 약 84.6MB, 시간 608ms로 괜찮은 속도를 보인다.

1. `*l = range(n + 1)`는 Syntax Error. `range`를 리스트로 받기 위해 `[*range(...)]`나 `list(range(...))`대신 저렇게 쓸 수 있는 것 같다.
2. `l`은 0, 1부터 시작하니 2부터 슬라이싱하고 반복문을 수행한다.
3. 슬라이스된 리스트의 각 원소들을 원래 리스트의 인덱스로 삼는다. 그 값이 m보다 크면 슬라이스된 리스트의 값을 출력한다.
   - When `i` is 2, `l[i]` is also 2, so that nothing is printed for the first loop if `m` is 1. 
4. It loops through the entire `l[2:]`.
5. After printing each element greater or equal to `m`, multiples of it is overwritten with 0, `len(l[i::i])` being `n // i`.
    - `n` is `len(l)`, `i` is how long `l` is cut off when sliced as `l[i]`.