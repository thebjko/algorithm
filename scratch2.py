from sys import setrecursionlimit
from collections import deque
setrecursionlimit(10**6)
g, *edges = open("input.txt")

class Search:
    def __init__(self, vertices: int, edges: int, start_vertex: int) -> None:
        """
        메서드 실행시 다시 초기화 할 필요가 없는 것들
        """
        self.graph:        list[list[int]] = [[] for _ in range(vertices + 1)]
        self.vertices:     int             = vertices
        self.start_vertex: int             = start_vertex
        self.edges:        int             = edges


    def add_edges(self, v1: int, v2: int) -> None:
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)


    def build_graph(self, reverse: bool = False):
        """
        양방향 간선을 갖는 그래프 그리기
        """
        for i in edges:
            a, b = map(int, i.split())
            self.add_edges(a, b)

        for i in self.graph:
            i.sort(reverse=reverse)    


    def initialize(self) -> None:
        """
        케이스마다 초기화해야할 변수들 초기화
        dfs, bfs메서드를 실행할 때 필요한 스택과 큐, 그리고 결과값을 저장할 self.result 초기화
        각 함수 내에서 초기화
        """
        self.cnt:    int             = 1
        self.tmp:    list[list[int]] = [[], []]
        self.stack:  list[int]       = [self.start_vertex]
        self.q:      deque[int]      = deque([self.start_vertex])
        self.result: dict[int, int]  = dict()


    # 메모리 약 83MB, 시간 660ms
    def bfs_with_deque(self) -> None:
        """
        True -> 인접 정점을 내림차순으로 방문
        False -> 인접 정점을 오름차순으로 방문
        """
        self.initialize()
        while self.q:
            v = self.q.popleft()
            if v not in self.result:
                self.result.update([(v, self.cnt)])
                self.cnt += 1
                for i in self.graph[v]:
                    if i not in self.result:
                        self.q.append(i)


    # 메모리 약 101MB, 시간 788ms
    def bfs_recursion_with_deque(self) -> None:
            if not self.q:
                return

            v = self.q.popleft()
            if v not in self.result:
                self.result.update([(v, self.cnt)])
                self.cnt += 1
                for i in self.graph[v]:
                    if i not in self.result:
                        self.q.append(i)
            self.bfs_recursion_with_deque()

    def bfs_recursive(self) -> None:
        """
        True -> 인접 정점을 내림차순으로 방문
        False -> 인접 정점을 오름차순으로 방문
        """
        self.initialize()
        # self.bfs_recursion_with_deque()
        self.bfs_recursion_without_deque(self.start_vertex)


    def bfs_recursion_without_deque(self, v: int) -> None:
        if v not in (r := self.result):
            r.update([(v, self.cnt)])
            self.cnt += 1

        # 메모리 약 92MB, 시간 1124ms
        def recursion(index: int, ls: list[int]) -> None:
            if not ls:
                return 
            for i in ls:
                if i not in (r := self.result):
                    r.update([(i, self.cnt)])
                    self.cnt += 1
            for i in ls:
                self.tmp[index] += [j for j in self.graph[i] if j not in r]
            # self.tmp[(index+1)&1] = []
            self.tmp[(index+1)&1].clear()   # 사용시 메모리 약 84MB, 시간 1056ms. 이로써 리스트의 모든 메서드를 사용해봤다.
            recursion((index+1)&1, self.tmp[index])

        recursion(0, self.graph[v])


    # 메모리 약 77MB, 시간 612ms
    def dfs_with_stack(self) -> None:
        """
        True -> 인접 정점을 오름차순으로 방문
        False -> 인접 정점을 내림차순으로 방문
        pop 메서드를 사용하기 때문(오름차순으로 append하면 내림차순으로 pop되기 때문에) ????
        """
        self.initialize()
        while self.stack:
            v = self.stack.pop()
            if v not in self.result:
                self.result.update([(v, self.cnt)])   # 방문처리
                self.cnt += 1
                for i in self.graph[v]:
                    self.stack.append(i)


    def dfs_recursive(self) -> None:
        """
        dfs_recursion_with_stack():
        True -> 인접 정점을 내림차순으로 방문
        False -> 인접 정점을 오름차순으로 방문

        dfs_recursion_without_stack():
        True -> 인접 정점을 내림차순으로 방문
        False -> 인접 정점을 오름차순으로 방문
        왜지??

        함수 호출이 정의보다 앞서도 된다.
        """
        self.initialize()
        self.dfs_recursion_with_stack()
        # self.dfs_recursion_without_stack(self.start_vertex)

    # 메모리 약 80MB, 시간 892ms
    def dfs_recursion_with_stack(self) -> None:
        if not self.stack:
            return
        v = self.stack.pop()
        if v not in self.result:
            self.result.update([(v, self.cnt)])
            self.cnt += 1    
            for i in self.graph[v]:
                if i not in self.result:
                    self.stack.append(i)
                self.dfs_recursion_with_stack()

    # 메모리 약 80MB, 시간 860ms
    def dfs_recursion_without_stack(self, v: int) -> None:
        # 종료조건 필요없음 (= v가 self.result에 있는 경우)
        if v not in self.result:
            self.result.update([(v, self.cnt)])
            self.cnt += 1
            for i in self.graph[v]:
                self.dfs_recursion_without_stack(i)


    def print_result(self) -> None:
        for i in range(self.vertices):
            print(self.result.get(i + 1, 0))


if __name__ == "__main__":
    n, m, r = map(int, g.split())
    s = Search(n, m, r)

    s.build_graph(True)

    # s.dfs_with_stack()
    # s.print_result()

    # s.dfs_recursive()
    # s.print_result()

    # s.bfs_with_deque()
    # s.print_result()

    s.bfs_recursive()
    s.print_result()