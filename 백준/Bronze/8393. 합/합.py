from functools import reduce

n = int(input())
hap = reduce(lambda x,y: x+y, range(1,n+1))
print(hap)