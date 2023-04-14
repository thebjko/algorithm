import sys
from collections import deque
sys.setrecursionlimit(500_000)


def solution(targets):
    targets.sort()
    q = deque(targets)

    def f(q: deque, mark: int = 0, answer: int = 0) -> int:
        if not q:
            return answer
        e = mark
        while q:
            x, y = q.popleft()
            if x >= e:
                answer += 1
                e = y
            elif y <= e:
                return f(q, y, answer)
        return answer
    return f(q)