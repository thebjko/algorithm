import sys
from collections import deque


input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    ls = deque(map(int, input().split()))

    radix = [0] * 10
    num = 0
    for idx, val in enumerate(ls):
        if idx == m:
            num = val
        radix[val] += 1
    
    order = 0
    k = 9
    while k > 0:
        while radix[k] and m >= 0:
            x = ls.popleft()
            if x == k:
                order += 1
                radix[k] -= 1

            else:
                ls.append(x)
            m -= 1
            if m < 0 and k != num:
                m = len(ls) - 1
        
        k -= 1

    print(order)