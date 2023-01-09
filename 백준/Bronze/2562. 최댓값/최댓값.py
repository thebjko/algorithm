a = list(map(int, open(0).read().split()))
m = max(a)
print(str(m)+'\n'+str(a.index(m)+1))