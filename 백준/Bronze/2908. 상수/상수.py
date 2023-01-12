(a := list(input())).reverse()
b = a[:3] < a[4:7]
print(''.join(a[4*b:3+4*b]))
