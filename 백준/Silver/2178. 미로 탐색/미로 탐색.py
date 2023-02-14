import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in ' '*N]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(q1, depth: int) -> None:
    q2 = deque()
    while q1:
        x, y = q1.popleft()
        if (x, y) == (M-1, N-1):
            return
        for dx, dy in d:
            a, b = x+dx, y+dy
            if 0<=a<M and 0<=b<N and maze[b][a] == 1:
                q2.append((a, b))
                maze[b][a] = depth
    bfs(q2, depth+1)


bfs(deque([(0, 0)]), 2)
print(maze[N-1][M-1])
