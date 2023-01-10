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

"""
숏코딩
for i in[*open(0)][1:]:
    a,*b=map(int,i.split())
    print(f'{sum(a*j>sum(b)for j in b)/a:.3%}')
    
"""