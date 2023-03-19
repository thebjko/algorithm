*ls, = open(0)

for i in ls[:-1]:
    i = i.rstrip()
    is_palindrome = True
    l, r = 0, len(i) - 1
    while l <= r:
        if i[l] == i[r]:
            l += 1
            r -= 1
            continue
        
        print('no')
        is_palindrome = False
        break

    if is_palindrome:
        print('yes')