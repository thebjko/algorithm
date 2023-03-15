from collections import deque
def solution(s: str):
    answer = 0
    cnt = [0, 0]
    q = deque(list(s))
    while q:
        x = q.popleft()
        cnt[0] += 1
        while cnt[0] != cnt[1] and q:
            y = q.popleft()
            if y == x:
                cnt[0] += 1
            else:
                cnt[1] += 1
        answer += 1
        cnt = [0, 0]

    return answer