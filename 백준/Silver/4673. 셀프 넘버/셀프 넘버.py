def d(n):
    s = n
    while n:   # walras 연산자를 쓰지 않아도 업데이트 된다.
        s += n%10
        n //= 10

    return s
    
t = list(range(10001))

for i in range(10001):
    if d(i) < 10001:
        try:
            t.remove(d(i))
        except:
            pass

# for i in t:
#     print(i)
print(*t)

"""
숏코딩
r=range(9999)
print(*sorted({*r}-{n+sum(map(int,str(n)))for n in r}))

# n+sum(map(int, str(n))) for n in r   => d(n) 함수의 역할
# 세트끼리의 연산 활용


"""