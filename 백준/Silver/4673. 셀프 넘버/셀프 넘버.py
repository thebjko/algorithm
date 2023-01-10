def d(n):
    s = n
    while n:
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

for i in t:
    print(i)