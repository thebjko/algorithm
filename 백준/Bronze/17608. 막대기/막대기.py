_, *ls = list(map(int, open(0).read().split()))

cnt = 0
h = 0
while ls:
    if (x := ls.pop()) > h:
        h = x
        cnt += 1

print(cnt)