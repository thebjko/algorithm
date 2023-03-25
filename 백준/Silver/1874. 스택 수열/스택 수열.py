n, *ls = map(int, open(0).read().split())
stack = [0]
result = ''

n = [*range(n, 0, -1)]
for i in ls:
    while stack[-1] < i:
        if not n:
            print('NO')
            exit()
        stack.append(n.pop())
        result += '+ '
    
    while stack[-1] > i:
        if stack[-1] == 0:
            print('NO')
            exit()
        stack.pop()
        result += '- '
    
    if stack[-1] == i:
        stack.pop()
        result += '- '
    
print(result)