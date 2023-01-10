score = 0
inc = 1
quiz = open(0).read().split()

for i in quiz[1:]:
    for j in i:
        if j == 'O':
            score += inc
            inc += 1
            # print(score
        else:
            inc = 1
    inc = 1
    print(score)
    score = 0