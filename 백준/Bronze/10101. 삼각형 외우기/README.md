# [Bronze IV] 삼각형 외우기 - 10101 

[문제 링크](https://www.acmicpc.net/problem/10101) 

### 성능 요약

메모리: 30616 KB, 시간: 48 ms

### 분류

기하학(geometry), 구현(implementation)

### 문제 설명

<p>창영이는 삼각형의 종류를 잘 구분하지 못한다. 따라서 프로그램을 이용해 이를 외우려고 한다.</p>

<p>삼각형의 세 각을 입력받은 다음, </p>

<ul>
	<li>세 각의 크기가 모두 60이면, Equilateral</li>
	<li>세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles</li>
	<li>세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene</li>
	<li>세 각의 합이 180이 아닌 경우에는 Error</li>
</ul>

<p>를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>총 3개의 줄에 걸쳐 삼각형의 각의 크기가 주어진다. 모든 정수는 0보다 크고, 180보다 작다.</p>

### 출력 

 <p>문제의 설명에 따라 Equilateral, Isosceles, Scalene, Error 중 하나를 출력한다.</p>

### 숏코딩 분석
```python
# originally
print(['Error','Equilateral','Isosceles','Scalene'][(sum(c:=[*map(int,open(0))])==180)*len({*c})])

# equivalently
ls = ['Error','Equilateral','Isosceles','Scalene']
c = [*map(int, open(0))]
print(ls[(sum(c) == 180) * len(set(c))])

```
입력값을 c에 받아서 합이 180이면 1 아니면 0.
c를 세트로 만들면 1일때 정삼각형, 2일때 이등변 삼각형 3일때 Scalene.