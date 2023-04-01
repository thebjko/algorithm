from collections import Counter

_, _, B, *ls = map(int, open(0).read().split())

radix = Counter(ls)

def f(case: int, inventory: int, time: int = 0):
    for height, count in radix.items():
        x = count * abs(height - case)
        if not x:
            continue
        if height > case:
            inventory += x
            time += x*2
        elif height < case:
            inventory -= x
            time += x

    if inventory < 0:
        return float('inf')
    
    return time


time, c = float('inf'), 0
for tc in range(min(radix), max(radix)+1):
    t = f(tc, B)
    if t <= time:
        time = t
        c = tc

print(time, c)