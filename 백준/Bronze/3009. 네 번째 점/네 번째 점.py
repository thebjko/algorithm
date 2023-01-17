ls = list(map(int, open(0).read().split()))
result = []
for i in (ls_1 := ls[0::2]):
    if ls_1.count(i) == 1:
        result.append(i)

for i in (ls_2 := ls[1::2]):
    if ls_2.count(i) == 1:
        result.append(i)

print(*result)
