a, b = list(map(int, open(0).read().split()))

ls =[]
for num in range(a, b + 1):
    k = 0
    if num == 1:
        continue
    elif num == 2:
        ls.append(2)   
    else:
        for i in range(2, num):
            if num % i == 0:
               break
            else:
                k += 1
                
        if num - k == 2:
            ls.append(num)

if ls:
    print(sum(ls), min(ls))
else:
    print(-1)
