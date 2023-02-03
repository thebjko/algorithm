# [Silver II] 좌표 압축 - 18870 

[문제 링크](https://www.acmicpc.net/problem/18870) 

### 성능 요약

메모리: 169636 KB, 시간: 2520 ms

### 분류

값 / 좌표 압축(coordinate_compression), 정렬(sorting)

### 문제 설명

<p>수직선 위에 N개의 좌표 X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>N</sub>이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.</p>

<p>X<sub>i</sub>를 좌표 압축한 결과 X'<sub>i</sub>의 값은 X<sub>i</sub> > X<sub>j</sub>를 만족하는 서로 다른 좌표의 개수와 같아야 한다.</p>

<p>X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>N</sub>에 좌표 압축을 적용한 결과 X'<sub>1</sub>, X'<sub>2</sub>, ..., X'<sub>N</sub>를 출력해보자.</p>

### 입력 

 <p>첫째 줄에 N이 주어진다.</p>

<p>둘째 줄에는 공백 한 칸으로 구분된 X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>N</sub>이 주어진다.</p>

### 출력 

 <p>첫째 줄에 X'<sub>1</sub>, X'<sub>2</sub>, ..., X'<sub>N</sub>을 공백 한 칸으로 구분해서 출력한다.</p>

### 다른 코드 분석
[cong2738님의 코드](https://www.acmicpc.net/source/52884830):
```python
from math import inf   # ?
N = int(input())
data = list(map(int,input().split()))
sorted_data = sorted(set(data))
data_dict = {x:i for i,x in enumerate(sorted_data)}
print(' '.join([str(data_dict[x]) for x in data]))
```
> 메모리 약 204MB, 시간 1380ms

1. inf는 사용하려다 만 것 같다.
2. 데이터를 받아서 셋, 및 정렬(오름차순)
3. 원소보다 낮은 숫자의 종류만큼 세야 하므로 각 원소당 인덱스로 묶어 딕셔너리에 추가
4. 원래 데이터로 딕셔너리의 데이터 호출

[nasoob114님의 코드](https://www.acmicpc.net/source/40037643):
```python
a,A=open(0);b=[*map(int,A.split())];B=dict(zip(sorted({*b}),range(9**9)));print(*(B[c]for c in b))

# Equivalenty:
a, A = open(0)
b = [*map(int, A.split())]
B = dict(zip(sorted({*b}), range(9 ** 9)))
print(*(B[c] for c in b))

```
> 메모리 약 153MB, 시간 1700ms

1. `A`는 두번째 줄을 문자열로 하나로 받는다.
2. `b`에 `A`를 `split()`하여 정수형으로 저장(리스트)
3. `b`를 `set`로, 정렬한 리스트를 `zip`함수를 사용해 0부터 `9**9 - 1`(387420488)까지의 수와 묶어준다.
    - 여기서 한쪽 이터러블의 숫자가 모자라면 그 이전까지만 `zip`된다는 것을 알 수 있다.
4. `b`의 각 원소들로 딕셔너리 `B`의 값들을 호출한다.