import sys

input = sys.stdin.readline

init = 1
for _ in range(int(input())):
    ls = list(map(int, input().split()))
    if init in ls:
        for i in ls:
            if i != init:
                init = i
                break

print(init)