cr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
n = len(s)
for i in cr:
    n -= s.count(i)

print(n)