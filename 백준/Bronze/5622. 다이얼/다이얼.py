chars = list(map(chr, range(65,91)))
ls = list(map(lambda x: (x-56)//3, range(65, 91)))
ls[chars.index('S')] -= 1
ls[ls.index(10)] -= 1
ls[ls.index(11)] -= 1
ls[ls.index(11)] -= 1

s = 0
for i in input():
    s += ls[chars.index(i)]

print(s)