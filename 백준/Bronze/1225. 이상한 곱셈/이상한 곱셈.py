a, b = input().split()
s = sum(map(int, a))
print(sum([s * int(i) for i in b]))