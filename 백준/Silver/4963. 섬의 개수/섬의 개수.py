import sys
from itertools import product

input = sys.stdin.readline

def dfs(graph: dict, start: tuple[int, int]) -> set[int]:
    explored, stack = {start, }, [start]

    while stack:
        v = stack.pop()
        explored.add(v)

        for adj in graph.get(v):
            if adj not in explored:
                stack.append(adj)
    
    return explored

delta = list(product([0, 1, -1], repeat=2))

while True:
    width, height = map(int, input().split())
    
    if width == height == 0:
        break

    matrix = [list(map(int, input().split())) for _ in range(height)]
    d = {(w, h): set() for w in range(width) for h in range(height) if matrix[h][w]}

    for l in d:
        for dx, dy in delta:
            (x, y) = l
            x += dx
            y += dy
            if x < 0 or y < 0 or x >= width or y >= height:
                continue
            
            if matrix[y][x]:
                d.get(l).add((x, y))

    cnt = 0
    s = set()
    for l in d:
        if l not in s:
            s = s.union(dfs(d, l))
            cnt += 1

    print(cnt)
