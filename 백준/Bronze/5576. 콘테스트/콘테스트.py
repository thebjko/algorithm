ls = list(map(int, open(0).read().split()))
print(sum(sorted(ls[:10])[-3:]))
print(sum(sorted(ls[10:])[-3:]))