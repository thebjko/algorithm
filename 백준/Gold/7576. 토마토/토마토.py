import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
M, N = map(int, input().split())
delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def bfs(q1: list[int]):
    if not q1:
        return
    q2 = []
    while q1:
        (x, y) = q1.pop()
        for dx, dy in delta:
            a, b = x+dx, y+dy
            if 0<=a<M and 0<=b<N and box[b][a] == 0:
               q2.append((a, b))
               box[b][a] = box[y][x] + 1
            else:
                continue
    bfs(q2)

no_zero = True
box = []
loc_tomatoes = []
for y in range(N):
    box.append(list(map(int, input().split())))
    for x in range(M):
        if box[y][x] == 0:
            no_zero = False
        if box[y][x] == 1:
            loc_tomatoes.append((x, y))

if no_zero:
    print(0)
else:
    bfs(loc_tomatoes)
    for i in box:
        if 0 in i:
            print(-1)
            break
    else:
        print(max(map(max, box)) - 1)