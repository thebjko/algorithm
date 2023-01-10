score = 0
inc = 1
quiz = open(0).read().split()

for i in quiz[1:]:
    for j in i:
        if j == 'O':
            score += inc
            inc += 1
        else:
            inc = 1
    inc = 1
    print(score)
    score = 0

"""
숏코딩
for i in[*open(0)][1:]:
    n=0
    print(sum((n:=(n+1)*(j=='O'))for j in i))
    
"""