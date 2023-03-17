_, *ls = open(0)
stack = []
for i in ls:
    i = i.strip()
    if 'push' in i:
        stack.append(i[5:])
    elif 'pop' in i:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif 'size' in i:
        print(len(stack))
    elif 'empty' in i:
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)