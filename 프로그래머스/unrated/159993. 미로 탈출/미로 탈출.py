from collections import deque

def solution(maps):
    points = {}
    dim = (len(maps[0]), len(maps))
    visited = [[0] * dim[0] for _ in range(dim[1])]
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for y in range(dim[1]):
        for x in range(dim[0]):
            if maps[y][x] == 'S':
                points['Start'] = (x, y)
            if maps[y][x] == 'E':
                points['End'] = (x, y)
            if maps[y][x] == 'L':
                points['Lever'] = (x, y)
    
    def bfs():
        nonlocal visited
        q, flag = deque(), 1
        q.append(p:=points['Start'])
        visited[p[1]][p[0]] = 1
        while q and flag:
            (x, y) = q.popleft()
            for dx, dy in delta:
                a, b = x+dx, y+dy
                if 0<=a<dim[0] and 0<=b<dim[1] and not maps[b][a] == 'X' and not visited[b][a]:
                    q.append((a, b))
                    visited[b][a] = visited[y][x] + 1
                    if (a, b) == points['Lever']:
                        l = visited[b][a]
                        visited = [[0] * dim[0] for _ in range(dim[1])]
                        visited[b][a] = l
                        q, flag = deque([(a, b)]), 0
                        break
        
        while q:
            (x, y) = q.popleft()
            for dx, dy in delta:
                a, b = x+dx, y+dy
                if 0<=a<dim[0] and 0<=b<dim[1] and not maps[b][a] == 'X' and not visited[b][a]:
                    q.append((a, b))
                    visited[b][a] = visited[y][x] + 1
                    if (a, b) == points['End']:
                        return visited[b][a] - 1
        
        return -1
                    
    
    answer = bfs()
    return answer