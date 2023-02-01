import sys

input = sys.stdin.readline

for _ in range(int(input())):
    ls = list(map(int, input().split()))
    ls.remove(max(ls))
    ls.remove(min(ls))
    if max(ls) - min(ls) >= 4:
        print("KIN")
    else:
        print(sum(ls))
