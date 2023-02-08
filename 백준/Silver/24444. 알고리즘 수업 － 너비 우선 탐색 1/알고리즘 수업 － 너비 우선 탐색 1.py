import sys
from collections import deque

input = sys.stdin.readline

class Graph:
    def __init__(self) -> None:
        self.vertices: dict[int, set[int]] = {}
        self.cnt: int = 1
    
    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        if from_vertex in self.vertices:
            self.vertices[from_vertex].add(to_vertex)
        else:
            self.vertices[from_vertex] = set((to_vertex, ))

    def bfs(self, start_vertex: int) -> dict[int, int]:
        queue: deque = deque()
        visited = dict([(start_vertex, self.cnt)])
        queue.append(start_vertex)
        while queue:
            vertex = queue.popleft()
            for adj in sorted(self.vertices.get(vertex, set())):
                if adj not in visited:
                    self.cnt += 1
                    visited.update([(adj, self.cnt)])
                    queue.append(adj)
        return visited

if __name__ == '__main__':
    g = Graph()

    n, m, r = map(int, input().split())
    for _ in range(m):
        a, b = map(int, input().split())
        g.add_edge(a, b)
        g.add_edge(b, a)

    d = g.bfs(r)

    for i in range(n):
        print(d.get(i + 1, 0))