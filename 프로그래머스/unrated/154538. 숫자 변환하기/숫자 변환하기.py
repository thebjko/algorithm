def solution(x, y, n):
    if x == y:
        return 0
    if x > y:
        return -1
    
    ls = [0] * y + [1]
    for i in range(y, x, -1):
        if ls[i]:
            if i%2 == 0 and i//2 >= 0:
                ls[i//2] = min(ls[i]+1, ls[i//2]) if ls[i//2] else ls[i]+1
            if i%3 == 0 and i//3 >= 0:
                ls[i//3] = min(ls[i]+1, ls[i//3]) if ls[i//3] else ls[i]+1
            if i-n >= 0:
                ls[i-n] = min(ls[i]+1, ls[i-n]) if ls[i-n] else ls[i]+1
                
    return ls[x]-1 if ls[x] else -1