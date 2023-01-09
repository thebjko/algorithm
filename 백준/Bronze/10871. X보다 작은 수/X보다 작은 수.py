numbers = list(map(int, open(0).read().split()))
ls = []

for i in numbers[2:]:
    if i < numbers[1]:
        ls.append(str(i))

print(' '.join(ls))

"""
숏코딩
_,x,*a=map(int,open(0).read().split())
for i in a:i<x!=print(i)
"""