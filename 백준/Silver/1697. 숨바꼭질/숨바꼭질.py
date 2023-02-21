import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

start, finish = map(int, input().split())
explored = set()
q1 = deque([start])
def bfs(q1: deque, time_lapse: int):
    q2: deque = deque()
    while q1:
        v = q1.popleft()
        if v == finish:
            print(time_lapse)
            return
        if v not in explored:
            explored.add(v)
            for i in [v+1, v-1, v*2]:
                if i >= 0 and i <= 100000:
                    q2.append(i)
    bfs(q2, time_lapse+1)
    
bfs(q1, 0)