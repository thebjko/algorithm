from sys import stdin
input = stdin.readline

N = int(input())
matrix = [list(map(int, input().strip())) for _ in ' ' * N]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = []
explored: set[tuple[int, int]] = set()
def dfs(start_vertex: tuple[int, int]) -> None:
    x, y = start_vertex
    if matrix[y][x]:
        explored.add(start_vertex)
        matrix[y][x] = 0
        for delta in range(4):
            a, b = x + dx[delta], y + dy[delta]
            if 0<=a<N and 0<=b<N:
                dfs((a, b))

for i in range(N):
    for j in range(N):
        dfs((i, j))
        if explored:
            ans.append(explored)
            explored = set()

print(len(ans))
print(*map(len, sorted(ans, key=len)))