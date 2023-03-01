_,a,_,b = open(0)
s = set(a.split())
print(*map(lambda x:1 if x in s else 0, b.split()))