K, N, *ls = map(int, open(0).read().split())

l, r = 1, max(ls)
f = lambda x: x//d
d, result = 0, 0
while l <= r:
    d = (l + r) // 2
    s = sum(map(f, ls))
    if s < N:
        r = d - 1
    elif s >= N:
        if d > result:
            result = d
        l = d + 1

print(result)