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

"""
숏코딩 분석
print(sum(5*min(ord(x),88)//16-17for x in input()))

s = 0
for x in input():
    s += 5 * min(ord(x), 88) // 16 - 17)

print(s)

이건 뭐 별수없다.
"""