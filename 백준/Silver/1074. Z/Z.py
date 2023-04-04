from itertools import cycle


N, r, c = map(int, input().split())
ls = [[0, 1], [2, 3]]

def z(r: int, c: int, N: int, answer: int = 0) -> int:
    if not N:
        print(answer)
        exit()
    
    idx = 0
    for i in cycle([0] * (2**(N-1)) + [1] * (2**(N-1))):
        if idx == r:
            R = i
            break
        idx += 1
    
    idx = 0
    for i in cycle([0] * (2**(N-1)) + [1] * (2**(N-1))):
        if idx == c:
            C = i
            break
        idx += 1
    
    answer += 2**(2*(N-1))*ls[R][C]

    z(r, c, N-1, answer)

    
z(r,c,N)