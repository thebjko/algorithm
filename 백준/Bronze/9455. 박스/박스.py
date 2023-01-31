# 박스
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    matrix = []
    rows, cols = map(int, input().split())
    for r in range(rows):
        matrix.append(list(map(int, input().split())))
    
    matrix.reverse()
    rotated = list(map(list, zip(*matrix)))

    cnt = 0
    for i in rotated:
        s = ''.join(map(str,i))
        while True:
            if "01" in s:
                s = s.replace("01", "10", 1)
                cnt += 1
            else: 
                break

    print(cnt)