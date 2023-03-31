ls = [*open(0)][:-1]
d = {
    ')': '(',
    ']': '[',
}
for i in ls:
    stack = []
    for char in i:
        if char in {'(', '['}:
            stack.append(char)
        elif char in d:
            if stack:
                x = stack.pop()
                if x == d[char]:
                    continue
                else:
                    print('no')
                    break
            else:
                print('no')
                break
    else:
        if stack:
            print('no')
        else:
            print('yes')