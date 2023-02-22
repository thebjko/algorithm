import sys
from collections import deque
input = sys.stdin.readline

delta = [(2, 1), (1, 2), (-1, -2), (-2, -1), (-1, 2), (1, -2), (2, -1), (-2, 1)]
for _ in range(int(input())):
    size = int(input())
    board = [[0] * size for _ in range(size)]
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    if start == end:
        print(0)
        continue
    q = deque([start])
    while q:
        (x, y) = q.popleft()
        for dx, dy in delta:
            a, b = x+dx, y+dy
            if not (0<=a<size and 0<=b<size) or board[b][a]:
                continue
            board[b][a] = board[y][x] + 1
            if (a, b) == end:
                print(board[b][a])
                q = 0
                break
            q.append((a, b))