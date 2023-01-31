# 누울 자리를 찾아라
import sys

input = sys.stdin.readline

N = int(input())
room = []
cnt = 0
for i in range(N):
    s = input().strip()
    room.append(s)
    for x in s.split("X"):
        if x >= "..":
            cnt += 1

print(cnt, end=" ")

rotated = list(map(list, zip(*room)))
cnt = 0
for i in rotated:
    s = "".join(i)
    for x in s.split("X"):
        if x >= "..":
            cnt += 1

print(cnt)