# 코드 최적화
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    matrix = []
    rows, _ = map(int, input().split())
    for _ in range(rows):
        matrix.append(input().split())
    
    transposed = zip(*matrix)

    cnt = 0
    for i in transposed:
        s = "".join(i)
        while (n := s.count("10")):
            s = s.replace("10", "01")
            cnt += n

    print(cnt)