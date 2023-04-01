# [Silver IV] 균형잡힌 세상 - 4949 

[문제 링크](https://www.acmicpc.net/problem/4949) 

# 코드 분석
## [kyuha0731 님의 코드 :](https://www.acmicpc.net/source/53432982)
```python
import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == ".":
        break
    if s.count("(") != s.count(")") or s.count("[") != s.count("]"):
        print("no")
        continue
    b = ""
    for i in s:
        if i in "()[]":
            b += i
    while "()" in b or "[]" in b:
        if "()" in b:
            b = b.replace("()", "")
        if "[]" in b:
            b = b.replace("[]", "")
    if b == "":
        print("yes")
    else:
        print("no")
```
> 메모리 약 31MB, 시간 52ms