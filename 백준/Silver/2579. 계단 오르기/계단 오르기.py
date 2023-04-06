n, *stair = map(int, open(0).read().split())

stair += [0, 0]
score = [0] * (n+2)

score[0] = stair[0]
score[1] = stair[1] + stair[0]
score[2] = max(stair[1], stair[0]) + stair[2]
for i in range(3, n):
    score[i] = stair[i] + max(stair[i-1] + score[i-3], score[i-2])

print(score[n-1])