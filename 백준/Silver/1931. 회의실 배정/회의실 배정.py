N, *ls = map(int, open(0).read().split())
ls = sorted(zip(ls[::2], ls[1::2]))

cnt = 0
e = 0
for i, j in ls:
    if i >= e:
        e = j
        cnt += 1
    else:
        if j < e:
            e = j
print(cnt)