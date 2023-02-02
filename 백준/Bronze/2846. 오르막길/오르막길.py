N, *ls = map(int, open(0).read().split())
d = [ls[i + 1] - ls[i] for i in range(N - 1)]

result = []
total = 0
for i in d:
    if i > 0:
        total += i
    else:
        result += [total]
        total = 0

result.append(total)
print(max(result))