a, b = open(0).read().split()

(a := list(map(int, a))).reverse()
(b := list(map(int, b))).reverse()

result = []
div = 0

if len(a) > len(b):
    for i in range(len(a)):
        try:
            a[i] += (b[i] + div)
            div, a[i] = divmod(a[i], 10)
        except:
            a[i] += div
            div, a[i] = divmod(a[i], 10)
        
            if div == 0:
                break
            else:
                continue
    
    if div == 1:
        a.append(1)

    result = a

elif len(b) > len(a):
    for i in range(len(b)):
        try:
            b[i] += (a[i] + div)
            div, b[i] = divmod(b[i], 10)
        except:
            b[i] += div
            div, b[i] = divmod(b[i], 10)

            if div == 0:
                break
            else: 
                continue

    if div == 1:
        b.append(1)

    result = b

else:
    for i, j in enumerate(b):
        a[i] += (j + div)
        div, a[i] = divmod(a[i], 10)

    if div == 1:
        a.append(div)

    result = a

(result := list(map(str, result))).reverse()
print("".join(result))
