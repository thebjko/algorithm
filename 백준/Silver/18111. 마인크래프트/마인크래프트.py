from collections import Counter

_, _, B, *ls = map(int, open(0).read().split())


radix = Counter(ls)

def f(case: int):
    inventory, time = B, 0
    for height, count in radix.items():
        if height == case:
            continue
        x = count * (height-case)
        inventory += x
        if height > case:
            time += x*2
        elif height < case:
            time -= x

    if inventory < 0:
        return float('inf')
    
    return time


time, c = float('inf'), 0
for tc in range(min(radix), max(radix)+1):
    t = f(tc)
    if t <= time:
        time = t
        c = tc

print(time, c)