ls = [[[0] * 101 for _ in range(101)] for _ in range(101)]

def f(a: int, b: int, c: int) -> int:
    if a <= 0 or b <= 0 or c <= 0:
        if not ls[a][b][c]:
            ls[a][b][c] = 1
        return ls[a][b][c]
    elif a > 20 or b > 20 or c > 20:
        if not ls[a][b][c]:
            ls[a][b][c] = f(20, 20, 20)
        return ls[a][b][c]
    elif a < b and b < c:
        if not ls[a][b][c]:
            ls[a][b][c] = f(a, b, c-1) + f(a, b-1, c-1) - f(a, b-1, c)
        return ls[a][b][c]
    else:
        if not ls[a][b][c]:
            ls[a][b][c] = f(a-1, b, c) + f(a-1, b-1, c) + f(a-1, b, c-1) - f(a-1, b-1, c-1)
        return ls[a][b][c]

for i in open(0):
    a, b, c = map(int, i.split())
    if a == b == c == -1:
        break
    print(f'w({a}, {b}, {c}) = {f(a,b,c)}')