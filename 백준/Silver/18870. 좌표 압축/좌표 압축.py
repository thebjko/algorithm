_, *ls = map(int, open(0).read().split())
sorted_ls = sorted(ls, reverse=True)
r = dict()
s = set()
result = []

ln = len(s)
while sorted_ls:
    s.add(n := sorted_ls.pop())
    if len(s) > ln:
        r.update([(n, ln)])
        ln = len(s)

for i in ls:
    result.append(r.get(i, 0))

print(*result)