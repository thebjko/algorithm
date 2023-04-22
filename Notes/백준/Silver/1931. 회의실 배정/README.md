# [Silver I] 회의실 배정 - 1931 

[문제 링크](https://www.acmicpc.net/problem/1931) 

### 성능 요약

메모리: 53684 KB, 시간: 172 ms

# 코드 분석
## [lycoris1600 님의 코드 :](https://www.acmicpc.net/source/58941379)
```python
a = e = 0
_, *l = map(int, open(0).read().split())
for i in sorted(zip(l[1::2], l[::2])):
 if e <= i[1]:
    e = i[0]
    a += 1
print(a)
```
> 메모리 약 54MB, 시간 168ms

내 코드와 비슷하나 약간 다르다.
1. 정렬
    - 끝점을 앞에 둬 끝점 기준으로 정렬했다: 끝점이 일찍 끝날수록 리스트 앞쪽에 위치한다.
2. 조건
    - 현재 시간표의 시작점을 이전 시간표의 끝과 비교한다(`e <= i[1]`): 이전 시간표의 끝이 현재 시간표의 시작보다 이르거나 같다면 현재 시간표의 끝을 e에 할당하고 1을 더 계수한다.
3. 해석
    - 끝점을 기준으로 정렬한데서 조건의 차이가 온다. 먼저 온 끝점을 기준으로 다음 카운트를 구하면 내가 else문 내에서 구했던 것처럼 더 이른 끝점으로 e를 재할당 할 필요가 없다.

## 내 코드 :
```python
N, *ls = map(int, open('input2.txt').read().split())
ls = sorted(zip(ls[::2], ls[1::2]))

cnt = 0
e = 0
for i, j in ls:
    if i >= e:
        e = j
        cnt += 1
    else:
        if j < e:
            e = j
print(cnt)
```
1. 나는 e가 현재 시간의 시작점보다 작으면, 마지막으로 재할당하고 cnt에 1을 더했다. 단, 이 경우는 e가 마지막보다 작을 경우 e에 j를 재할당해야한다.