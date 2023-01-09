numbers = list(map(int, open(0).read().split()))
s = set()
for i in numbers:
    s.add(i%42)

print(len(s))