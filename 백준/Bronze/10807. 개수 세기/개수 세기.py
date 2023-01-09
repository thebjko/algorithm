ls = list(open(0).read().split())

n = 0
for i in ls[1:-1]:
    if ls[-1] == i:
        n += 1

print(n)