T = open(0).read().split()

n = 0
for i in T[1]:
    n += int(i)

print(n)

"""
print(*map(int, '12353246'))   # 1 2 3 5 3 2 4 6
"""