# [Bronze III] 세탁소 사장 동혁 - 2720 

[문제 링크](https://www.acmicpc.net/problem/2720) 

### 성능 요약

메모리: 30616 KB, 시간: 92 ms

### 분류

사칙연산(arithmetic), 그리디 알고리즘(greedy), 수학(math)

### 문제 설명

<p>미국으로 유학간 동혁이는 세탁소를 운영하고 있다. 동혁이는 최근에 아르바이트로 고등학생 리암을 채용했다.</p>

<p>동혁이는 리암에게 실망했다.</p>

<p>리암은 거스름돈을 주는 것을 자꾸 실수한다.</p>

<p>심지어 <span>$</span>0.5달러를 줘야하는 경우에 거스름돈으로 <span>$</span>5달러를 주는것이다!</p>

<p>어쩔수 없이 뛰어난 코딩 실력을 발휘해 리암을 도와주는 프로그램을 작성하려고 하지만, 디아블로를 하느라 코딩할 시간이 없어서 이 문제를 읽고 있는 여러분이 대신 해주어야 한다.</p>

<p>거스름돈의 액수가 주어지면 리암이 줘야할 쿼터(Quarter, <span>$</span>0.25)의 개수, 다임(Dime, <span>$</span>0.10)의 개수, 니켈(Nickel, <span>$</span>0.05)의 개수, 페니(Penny, <span>$</span>0.01)의 개수를 구하는 프로그램을 작성하시오. 거스름돈은 항상 <span>$</span>5.00 이하이고, 손님이 받는 동전의 개수를 최소로 하려고 한다. 예를 들어, <span>$</span>1.24를 거슬러 주어야 한다면, 손님은 4쿼터, 2다임, 0니켈, 4페니를 받게 된다.</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 거스름돈 C를 나타내는 정수 하나로 이루어져 있다. C의 단위는 센트이다. (1달러 = 100센트) (1<=C<=500)</p>

### 출력 

 <p>각 테스트케이스에 대해 필요한 쿼터의 개수, 다임의 개수, 니켈의 개수, 페니의 개수를 공백으로 구분하여 출력한다.</p>

### 다른 코드 분석
```python
for i in[*open(0)][1:]:
    c = int(i)
    print(c // 25, c % 25 // 10, c % 25 // 5 % 2, c % 5)

```
첫 번째, 두 번째, 네 번째는 이해가 직관적으로 간다. 세 번째는 무엇인가?  
두 번째는 거스름돈을 25로 나눈 나머지를 10으로 나눈 몫, 세 번째는 거스름돈을 25로 나눈 나머지를 5로 나눈 몫을 2로 나눈 나머지? `c % 25 % 10 // 5`여야 하는거 아닌가? 생각해보자. 10은 5의 배수니까 5가 2개 이상 될 리가 없다. 즉 거스름돈을 25로 나눈 나머지를 5로 나눈 몫에 2를 나눈 몫이 10으로 나눈 몫 * 2가 된다.