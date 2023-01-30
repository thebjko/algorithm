ls = [sum(map(int, input().split())) for _ in range(5)]
print(ls.index(max(ls)) + 1, max(ls))