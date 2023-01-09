num = [*range(1,31)]

for i in list(map(int, open(0).read().split())):
    num.remove(i)

for i in num:
    print(i)