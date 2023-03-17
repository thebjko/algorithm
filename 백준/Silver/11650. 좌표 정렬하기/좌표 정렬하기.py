_, *ls = map(int, open(0).read().split())
for i in sorted(sorted(zip(ls[::2], ls[1::2]), key=lambda x: x[1]), key=lambda x: x[0]):
    print(*i)