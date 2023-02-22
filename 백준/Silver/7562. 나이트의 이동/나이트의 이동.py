import sys
from collections import deque
input = sys.stdin.readline

delta = [(2, 1), (1, 2), (-1, -2), (-2, -1), (-1, 2), (1, -2), (2, -1), (-2, 1)]
for _ in range(int(input())):
    size = int(input())
    board = [[0] * size for _ in range(size)]
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    q = deque([start])
    while q:
        (x, y) = q.popleft()
        if (x, y) == end:
            print(board[y][x])
            break
        for dx, dy in delta:
            a, b = x+dx, y+dy
            if not (0<=a<size and 0<=b<size) or board[b][a]:
                continue
            board[b][a] = board[y][x] + 1
            q.append((a, b))