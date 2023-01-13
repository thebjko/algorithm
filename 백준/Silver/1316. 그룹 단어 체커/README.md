# [Silver V] 그룹 단어 체커 - 1316 

[문제 링크](https://www.acmicpc.net/problem/1316) 

### 성능 요약

메모리: 30616 KB, 시간: 36 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.</p>

<p>단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.</p>

### 출력 

 <p>첫째 줄에 그룹 단어의 개수를 출력한다.</p>

### 숏코딩 분석
```python
# original(space added)
print(sum([*x] == sorted(x, key=x.find) for x in open(0)) - 1)

# equivalently
n = 0
for word in open(0):
    # 문자열의 find 메서드는 substring의 가장 작은 인덱스를 반환한다.
    # sorted 함수는 리스트를 반환한다.
    # 리스트로 변환된 단어가 한 문자가 단어에 처음 나타난 순서대로 정렬되었을 때와 같다면 n에 1을 더한다.
    if [*word] == sorted(word, key=word.find):
        n += 1

print(n - 1)
```