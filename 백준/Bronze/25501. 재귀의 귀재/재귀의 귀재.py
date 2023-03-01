def recursion(s: str, l: int, r: int) -> int:
    global cnt
    cnt += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)
    
def is_palindrome(s: str) -> int:
    return recursion(s, 0, len(s)-1)

for s in open(0).read().splitlines()[1:]:
    cnt = 0
    print(is_palindrome(s), cnt)