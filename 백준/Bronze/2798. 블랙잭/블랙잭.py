import sys

input = sys.stdin.readline

n, m = map(int, input().split())
iter = list(map(int, input().split()))
ls = []
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if (x := iter[i] + iter[j] + iter[k]) <= m:
                ls.append(x)

print(max(ls))