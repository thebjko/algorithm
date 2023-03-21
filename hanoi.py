def r(idx: int, k: int):
    while stack[idx]:
        if not stack[k]:
            return
        x = stack[idx].pop()
        D = 2 - ((n%2)^(x%2))
        where_to = (idx+D)%3

        if not stack[where_to] or stack[where_to][-1] > x:
            stack[where_to].append(x)
            print(idx+1, where_to+1)
        else:
            stack[idx].append(x)
            r(where_to, k)

def do(k: int = 0):
    print(stack)
    if stack[2]:
        x = stack[2].pop()
        if x == 1:
            return
    
    r(k, k)
    do(k^1)

n = int(input())
stack = [[*range(n, 0, -1)], [], []]

cnt = 0
for _ in range(n):
    cnt = cnt * 2 + 1
print(cnt)

do()