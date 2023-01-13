import sys

sys.stdin = open('input_UDLR.txt')

n = int(input())

x = y = 1

plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i, j in enumerate(move_types):
        if plan == j:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    else:
        x, y = nx, ny

print(x, y)