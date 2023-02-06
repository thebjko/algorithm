# 바이러스
import sys

input = sys.stdin.readline

input()
p = int(input())
d = dict()


for _ in range(p):
    a, b = map(int, input().split())
    if not d.get(a):
        d.update([(a, set())])
    if not d.get(b):
        d.update([(b, set())])

    d.get(a).add(b)       
    d.get(b).add(a)

def dfs(graph: dict, start: int) -> set[int]:
    explored, stack = {start, }, [start]

    while stack:
        v = stack.pop()
        explored.add(v)

        for adj in sorted(graph.get(v)):
            if adj not in explored:
                stack.append(adj)

    return explored

print(len(dfs(d, 1)) - 1)