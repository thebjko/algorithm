from statistics import mean

scores = list(map(int, open(0).read().split()))
modified = scores[1:]
m = max(modified)

for i, j in enumerate(modified):
    modified[i] = j/m*100

print(mean(modified))