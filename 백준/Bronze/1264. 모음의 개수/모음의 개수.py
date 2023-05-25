import sys
input = sys.stdin.readline

while True:
    x = input()
    if x.strip() == '#':
        break
    
    cnt = 0
    for i in x:
        if i in set('aeiouAEIOU'):
            cnt += 1
    print(cnt)