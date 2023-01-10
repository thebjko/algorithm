i = int(input())

ls = []
result = 0

if i < 100:
    print(i)
else:
    for n in range(100, i+1):
        while n:
            ls.append(n%10)
            n //= 10
        if ls[0]-ls[1] == ls[1]-ls[2]:
            try:
                if ls[1]-ls[2] == ls[2]-ls[3]:
                    result += 1
            except:
                result += 1
            finally:
                ls = []
        else:
            ls = []

    print(result+99)
