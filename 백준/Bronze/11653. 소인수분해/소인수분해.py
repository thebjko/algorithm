from math import prod

n = m = int(input())

ls = [1]
i = 2
while prod(ls) != m:
    if n % i == 0:
        ls.append(i)
        n //= i
    else:
        i += 1
    
ls.remove(1)
print(*ls)