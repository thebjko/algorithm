import sys

i = sys.stdin.readline

while True:
    ls = list(map(int, i().split()))
    
    if sum(ls) == 0:
        break    

    a = ls.pop(ls.index(min(ls)))
    b = ls.pop(ls.index(min(ls)))
    
    if a ** 2 + b ** 2 == ls[0] ** 2:
        print("right")

    else:
        print("wrong")