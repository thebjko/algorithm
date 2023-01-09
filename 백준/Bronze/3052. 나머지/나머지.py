numbers = list(map(int, open(0).read().split()))
s = set()
for i in numbers:
    s.add(i%42)

print(len(s))

"""
숏코딩 - 세트 컴프리헨션 사용
print(len({int(i)%42for i in open(0)}))
"""