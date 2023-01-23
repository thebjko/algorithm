_, *a = list(map(int, open(0).read().split()))

n = 0
for num in list(a):
    k = 0
    if num > 2:
        for divider in range(2, num):
            if num % divider != 0:
                k += 1
        
        if num - k == 2:
            n += 1

    elif num != 1:
        n += 1

print(n)