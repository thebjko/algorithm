n = m = int(input())

x = 1
i = 2
while x != m:
    if n % i == 0:
        x *= i
        n //= i
        print(i)
        
    else:
        i += 1
