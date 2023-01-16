_, *a = list(open(0).read().split())
n = 0
inc = 1
for i in a:
    if i == '1':
        n += inc
        inc += 1
    else:
        inc = 1

print(n)