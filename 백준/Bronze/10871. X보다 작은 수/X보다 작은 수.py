numbers = list(map(int, open(0).read().split()))
ls = []

for i in numbers[2:]:
    if i < numbers[1]:
        ls.append(str(i))

print(' '.join(ls))