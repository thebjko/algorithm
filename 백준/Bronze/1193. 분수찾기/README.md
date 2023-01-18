# [Bronze I] 분수찾기 - 1193 

[문제 링크](https://www.acmicpc.net/problem/1193) 

### 성능 요약

메모리: 270224 KB, 시간: 308 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p>무한히 큰 배열에 다음과 같이 분수들이 적혀있다.</p>

<table class="table table-bordered" style="width:30%">
	<tbody>
		<tr>
			<td style="width:5%">1/1</td>
			<td style="width:5%">1/2</td>
			<td style="width:5%">1/3</td>
			<td style="width:5%">1/4</td>
			<td style="width:5%">1/5</td>
			<td style="width:5%">…</td>
		</tr>
		<tr>
			<td>2/1</td>
			<td>2/2</td>
			<td>2/3</td>
			<td>2/4</td>
			<td>…</td>
			<td>…</td>
		</tr>
		<tr>
			<td>3/1</td>
			<td>3/2</td>
			<td>3/3</td>
			<td>…</td>
			<td>…</td>
			<td>…</td>
		</tr>
		<tr>
			<td>4/1</td>
			<td>4/2</td>
			<td>…</td>
			<td>…</td>
			<td>…</td>
			<td>…</td>
		</tr>
		<tr>
			<td>5/1</td>
			<td>…</td>
			<td>…</td>
			<td>…</td>
			<td>…</td>
			<td>…</td>
		</tr>
		<tr>
			<td>…</td>
			<td>…</td>
			<td>…</td>
			<td>…</td>
			<td>…</td>
			<td>…</td>
		</tr>
	</tbody>
</table>

<p>이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.</p>

<p>X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.</p>

### 출력 

 <p>첫째 줄에 분수를 출력한다.</p>

### 숏코딩
내 코드는 파이썬은 안되고 PyPy3로 제출해야 맞았다는 판정을 받는다.
time 라이브러리로도 0.1846 초 정도가 나오는데 왜 그럴까?
숏코딩과 비교했을 때 메모리도 9배정도 차이가 난다. 어디가 비효율적이었던 걸까?  

아래는 숏코딩이다.
```python
# Originally:
n=int(input());a=0
while n>0:a+=1;n-=a
print("%d/%d"%(1-n,a+n)[::a%2*2-1])

# Equivalently:
n = int(input())
a = 0

while n > 0:
	a += 1
	n -= a

print("%d/%d"%(1-n,a+n)[::a%2*2-1])   # 무슨 뜻일까
```
확실히 더 간결하긴 하다. 정말 필요한 부분만 추린 느낌?  
마지막 줄을 이해하기 위해 아래의 코드를 참고하면 좋을 것 같다.
```python
('a', 'b')[::-1]
>>> ('b', 'a')
```