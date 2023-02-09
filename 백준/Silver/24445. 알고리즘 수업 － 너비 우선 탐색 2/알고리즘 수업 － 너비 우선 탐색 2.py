from sys import *
from collections import deque
setrecursionlimit(10**6)
g, *edges = open(0)

class Search:
    def __init__(self, vertices: int, edges: int, start_vertex: int) -> None:
        self.graph:        list[list[int]] = [[] for _ in range(vertices + 1)]
        self.vertices:     int             = vertices
        self.start_vertex: int             = start_vertex
        self.edges:        int             = edges
        self.cnt:          int             = 1
        self.result:       dict[int, int]  = dict()

    def add_edges(self, v1: int, v2: int) -> None:
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def build_graph(self, reverse: bool = False):
        for i in edges:
            a, b = map(int, i.split())
            self.add_edges(a, b)

        for i in self.graph:
            i.sort(reverse=reverse)

        stdin.close()
    
    def prepare(self) -> None:
        self.q:     deque[int] = deque([self.start_vertex])


    def bfs(self, reverse: bool = False) -> None:
        self.build_graph(reverse)
        self.prepare()

        while self.q:
            v = self.q.popleft()
            if v not in self.result:
                self.result.update([(v, self.cnt)])
                self.cnt += 1
                for i in self.graph[v]:
                    if i not in self.result:
                        self.q.append(i)

    def print_result(self) -> None:
        for i in range(self.vertices):
            print(self.result.get(i + 1, 0))

        self.__init__(self.vertices, self.edges, self.start_vertex)
        

if __name__ == "__main__":
    n, m, r = map(int, g.split())
    s = Search(n, m, r)

    s.bfs(True)
    s.print_result()