hm = input()
hm = hm.split(sep=' ')
h = int(hm[0])
m = int(hm[1])

t = h * 60 + m
if h == 0:
    if m >= 45:
        m -= 45
    else:
        t += 15
        h = 23
        m = t % 60
else:
    t -= 45
    h = t // 60
    m = t % 60

print(h, m)