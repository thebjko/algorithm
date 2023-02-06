# [Bronze I] 행복한지 슬픈지 - 10769 

[문제 링크](https://www.acmicpc.net/problem/10769) 

### 성능 요약

메모리: 31256 KB, 시간: 40 ms

### 분류

파싱(parsing), 문자열(string)

### 문제 설명

<p>승엽이는 자신의 감정을 표현하기 위해서 종종 문자 메시지에 이모티콘을 넣어 보내곤 한다. 승엽이가 보내는 이모티콘은 세 개의 문자가 붙어있는 구조로 이루어져 있으며, 행복한 얼굴을 나타내는 <strong>:-)</strong> 와 슬픈 얼굴을 나타내는 <strong>:-(</strong> 가 있다.</p>

<p>혜성이는 승엽이의 이모티콘을 귀여운 척이라고 생각해 매우 싫어하므로, 승엽이의 문자가 오면 전체적인 분위기만 판단해서 알려주는 프로그램을 작성하고 싶다.</p>

### 입력 

 <p>첫 줄에 최소 1개에서 최대 255개의 문자들이 입력된다.</p>

### 출력 

 <p>출력은 다음 규칙에 따라 정해진다.</p>

<ul>
	<li>어떤 이모티콘도 포함되어 있지 않으면, <strong>none </strong>을 출력한다.</li>
	<li>행복한 이모티콘과 슬픈 이모티콘의 수가 동일하게 포함되어 있으면, <strong>unsure</strong> 를 출력한다.</li>
	<li>행복한 이모티콘이 슬픈 이모티콘보다 많이 포함되어 있으면, <strong>happy</strong> 를 출력한다.</li>
	<li>슬픈 이모티콘이 행복한 이모티콘보다 많이 포함되어 있으면, <strong>sad</strong> 를 출력한다.</li>
</ul>

### 다른 코드 분석

[joonion님의 코드](https://www.acmicpc.net/source/53804388):
```python
a,b=map(input().count,[':-)',':-('])
print(["none","unsure","sad","happy"][(a|b>0)+(a!=b)+(a>b)])

# Equivalently:
a, b = map(input().count, [':-)', ':-('])
print(["none","unsure","sad","happy"][(a | b > 0) + (a != b) + (a > b)])
```
>  메모리 약 31MB, 시간 36ms

1. 각 이모티콘을 입력값의 `count`메서드에 인자값을 넘긴다. 이때, `input()` 함수는 한번만 호출된다.
2. 버티컬바 `|`는 비트단위 `or` 연산자이다. 
	- 일단 `a`가 `b`보다 더 크면 1이 더해지고, 같지 않으면 또 1이 더해진다.
	- [`a | b`가 0보다 같거나 작을 경우가 언제 있을까?](https://jays-log1111.tistory.com/entry/4-2-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B9%84%ED%8A%B8%EC%97%B0%EC%82%B0%EC%9E%90-2%EC%9D%98-%EB%B3%B4%EC%88%98-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0#:~:text=%EA%B0%80%EC%9E%A5%20%EC%99%BC%EC%AA%BD%20%EB%B9%84%ED%8A%B8%EA%B0%80%200,%EB%9D%BC%EB%8A%94%20%EA%B2%83%EC%9D%84%20%EC%95%8C%20%EC%88%98%20%EC%9E%88%EC%8A%B5%EB%8B%88%EB%8B%A4.)
	- 양쪽이 다 양수이므로 음수가 될 경우는 없다.
	- 둘다 0일때만 0이된다. 즉 두 이모티콘이 없을 때 `False`, 하나라도 있으면 `True`.