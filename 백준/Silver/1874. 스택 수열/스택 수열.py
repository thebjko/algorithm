n, *ls = map(int, open(0).read().split())
stack = [0]
result = []

k = 1
for i in ls:
    while stack[-1] < i:
        if k > n:
            print('NO')
            exit()
        stack.append(k)
        k += 1
        result.append('+')
    
    while stack[-1] > i:
        if stack[-1] == 0:
            print('NO')
            exit()
        stack.pop()
        result.append('-')
    
    if stack[-1] == i:
        stack.pop()
        result.append('-')
    
print(' '.join(result))