s = open(0).read().split()

for i, j in enumerate(s[2::2]):
    p = j*int(s[1::2][i])
    for k in range(l := len(j)):
        print(p[k::l], end='')
    print('')
