import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    a, b = map(int, input().split())
    a %= 10
    if a == 0:
        print(10)
    elif a in {1, 5, 6}:
        print(a)
    elif a == 2:
        print([2, 4, 8, 6][(b-1)%4])
    elif a == 3:
        print([3, 9, 7, 1][(b-1)%4])
    elif a == 4:
        print([4, 6][(b-1)%2])
    elif a == 7:
        print([7, 9, 3, 1][(b-1)%4])
    elif a == 8:
        print([8, 4, 2, 6][(b-1)%4])
    elif a == 9:
        print([9, 1][(b-1)%2])