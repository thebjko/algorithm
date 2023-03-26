import sys

N = int(sys.stdin.readline().rstrip())
lst = []
for i in range((N // 2)):
    lst.append(max(map(int, sys.stdin.readline().rstrip().split())))
for i in range((N // 2), N - 1):
    lst += sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)[:(N + 1) // (N - i) + 1]
lst += list(map(int, sys.stdin.readline().rstrip().split()))

lst.sort()
print(lst[-N])