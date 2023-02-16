ls = list(map(int, open(0).read().split()))
a, b = divmod(i:=ls.index(m := max(ls)), 9)
print(m, a+1, b+1)