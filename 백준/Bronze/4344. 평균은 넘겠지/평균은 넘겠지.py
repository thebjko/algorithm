c = int(input())

while c:
    ls = list(map(int, input().split()))
    m = sum(ls[1:])/len(ls[1:])
    o = 0
    for i in ls[1:]:
        if i > m:
            o += 1
    print(f'{o/len(ls[1:])*100:.3f}%')
    c -= 1
