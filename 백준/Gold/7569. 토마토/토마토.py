import sys
sys.setrecursionlimit(10**6)
M, N, H, *ls = map(int, open(0).read().split())

no_zero = True
loc_tomatoes = []
for i, j in enumerate(ls):
    if j == 0:
        no_zero = False
    elif j == 1:
        loc_tomatoes.append(i)

if no_zero:
    print(0)
else:
    size = M*N*H
    level = M*N
    def bfs(q1: list, depth: int = 2):
        if not q1:
            return
        q2 = []
        while q1:
            x = q1.pop()
            if 0<=(k:=x+1)<size and k//M == x//M and ls[k] == 0:
                ls[k] = depth
                q2.append(k)
            if 0<=(k:=x-1)<size and k//M == x//M and ls[k] == 0:
                ls[k] = depth
                q2.append(k)
            if 0<=(k:=x+M)<size and k//level == x//level and ls[k] == 0:
                ls[k] = depth
                q2.append(k)
            if 0<=(k:=x-M)<size and k//level == x//level and ls[k] == 0:
                ls[k] = depth
                q2.append(k)
            if 0<=(k:=x+level)<size and ls[k] == 0:
                ls[k] = depth
                q2.append(k)
            if 0<=(k:=x-level)<size and ls[k] == 0:
                ls[k] = depth
                q2.append(k)
        bfs(q2, depth+1)

    bfs(loc_tomatoes)
    if 0 in ls:
        print(-1)
    else:
        print(max(ls)-1)