# [Silver IV] 나는야 포켓몬 마스터 이다솜 - 1620 

[문제 링크](https://www.acmicpc.net/problem/1620) 

### 성능 요약

메모리: 47056 KB, 시간: 248 ms

# 코드 분석
## [ttasjwi 님의 코드 :](https://www.acmicpc.net/source/56042254)
```python
import sys

lines = sys.stdin.buffer.read().decode().splitlines()

n, m = map(int, lines[0].split())
dic = {word: str(idx + 1) for idx, word in enumerate(lines[1:n + 1])}
answer = '\n'.join(lines[int(line)] if line.isdigit() else dic[line] for line in lines[1 + n:])
print(answer)
```
> 메모리 약 62MB, 시간 132ms