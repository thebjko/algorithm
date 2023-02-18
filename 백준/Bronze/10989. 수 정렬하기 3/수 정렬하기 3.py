import sys
input = sys.stdin.readline
N = int(input())
a = [0] * 10_001
for _ in ' '*N:
    i = int(input())
    a[i] += 1

for i in range(1, 10_001):
    for _ in ' '*a[i]:
        print(i)