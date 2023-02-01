from itertools import product
n = input()
ls = []
for k in reversed(range(len(n) + 1)):
    for i in eval("product(" + "['4', '7']," * k + ")"):
        m = int("".join(i))
        if m <= int(n):
            ls.append(m)

    if ls:
        print(max(ls))
        break