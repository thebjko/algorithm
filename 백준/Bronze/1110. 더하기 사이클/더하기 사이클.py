num = [open(0).read().strip()]

i = 0
while (num := num):
    n = num[i]
    if len(n) > 1:
        a, b = n[0], n[1]
    else:
        num[i] = '0' + num[i]
        a, b = '0', n[-1]
    
    c = str(int(a) + int(b))
    d = c[-1]
    e = b + d
    num.append(e)
    i += 1
    
    if num[-1] == num[0]:
        print(len(num)-1)
        break
