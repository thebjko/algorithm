def f(n: int, m: int = 0):
    if n == 0:
        return
    print(' ' * (n-1) + '*' * m, end='')
    print('*', end='')
    g(n, m)
    if m > 0:
        print('*' + '*' * (m-1))
    

def g(n: int, m: int):
    print('*' * m)
    f(n-1, m+1)
    print(' ' * n + '*' * (m-1), end='')


f(int(input()))