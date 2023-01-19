ls = open(0).read().split()[1:]
ls = zip(ls[::2], ls[1::2])
employees = {}
employees.update(ls)
print(*sorted([i for i, j in employees.items() if j == 'enter'], reverse=True))