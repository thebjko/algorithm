import sys

input = sys.stdin.readline

for _ in range(int(input())):
    matrix = []
    rows, _ = map(int, input().split())
    for _ in range(rows):
        matrix.append(input().split())
    
    rotated = list(map(list, zip(*matrix)))

    cnt = 0
    for i in rotated:
        s = ''.join(i)
        while "10" in s:
            cnt += s.count("10")
            s = s.replace("10", "01")

    print(cnt)