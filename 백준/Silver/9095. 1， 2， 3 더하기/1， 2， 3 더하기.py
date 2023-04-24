_, *ls = map(int, open(0).read().split())

def dfs(x: int):
    stack = [1, 2, 3]
    answer = 0
    while stack:
        u = stack.pop()
        if u == x:
            answer += 1
        for i in (1, 2, 3):
            v = u + i
            if v > x:
                continue
            stack.append(v)

    return answer

for i in ls:
    print(dfs(i))