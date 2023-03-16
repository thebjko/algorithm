from operator import itemgetter
_, *ls = open(0).read().split()
for i in sorted(zip(map(int, ls[::2]), ls[1::2]), key=itemgetter(0)):
    print(*i)