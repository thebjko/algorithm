# [Silver IV] 듣보잡 - 1764 

[문제 링크](https://www.acmicpc.net/problem/1764) 

> 메모리: 52404 KB, 시간: 96 ms

# 코드 분석
## [20210805 님의 코드 :](https://www.acmicpc.net/source/53955597)
```python
import os

arr = sorted(os.read(0, os.fstat(0).st_size).split()[2:])
result = [a for a, b in zip(arr, arr[1:]) if a == b]
os.write(1, b"%d\n" % len(result))
os.write(1, b"\n".join(result))
```
> 메모리 약 39MB, 시간 52ms

간단한 로직이지만 문제 조건을 잘 파악해야 구현할 수 있는 알고리즘이다.