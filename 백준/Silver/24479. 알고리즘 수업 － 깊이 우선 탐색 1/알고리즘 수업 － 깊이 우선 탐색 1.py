import sys

input = sys.stdin.readline

class Graph:
    def __init__(self) -> None:
        self.vertices: dict[int, list[int]] = {}
    
    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        if from_vertex in self.vertices:
            self.vertices[from_vertex].append(to_vertex)
        else:
            self.vertices[from_vertex] = [to_vertex]

    def dfs(self, start_vertex: int) -> dict[int, int]:
        cnt = 2
        explored, stack = {start_vertex: 1}, [start_vertex]
        while stack:
            vertex = stack.pop()
            if vertex not in explored:
                explored.update([(vertex, cnt)])
                cnt += 1
            for adj in sorted(self.vertices.get(vertex, []), reverse=True):
                if adj not in explored:
                    stack.append(adj)

        return explored

if __name__ == '__main__':
    n, m, r = map(int, input().split())

    g = Graph()

    for _ in range(m):
        a, b = map(int, input().split())
        g.add_edge(a, b)
        g.add_edge(b, a)

    d = g.dfs(r)

    for i in range(n):
        print(d.get(i + 1, 0))