from operator import itemgetter
_, *ls = map(int, open(0).read().split())
for i in sorted(sorted(zip(ls[::2], ls[1::2]), key=itemgetter(0)), key=itemgetter(1)):
    print(*i)