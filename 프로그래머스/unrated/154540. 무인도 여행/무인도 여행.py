delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def solution(maps):
    X, Y = len(maps[0]), len(maps)
    visited = [[False] * X for _ in range(Y)]
    stack, answer = [], []
    for i in range(X):
        for j in range(Y):
            if maps[j][i] != 'X' and not visited[j][i]:
                stack.append((i, j))
                visited[j][i] = True
                days = int(maps[j][i])
                while stack:
                    x, y = stack.pop()
                    for dx, dy in delta:
                        a, b = x+dx, y+dy
                        if (0<=a<X and 0<=b<Y) and maps[b][a] != 'X' and not visited[b][a]:
                            visited[b][a] = True
                            days += int(maps[b][a])
                            stack.append((a, b))
                
                answer.append(days)

    return sorted(answer) if answer else [-1]