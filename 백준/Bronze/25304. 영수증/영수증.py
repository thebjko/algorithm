n = list(map(int, open(0).read().split()))
nn = n[2:]

total = 0
l = int(len(nn)/2)
for i in range(l):
    total += (nn[i*2] * nn[i*2+1])

if total == n[0]:
    print('Yes')
else:
    print('No')
