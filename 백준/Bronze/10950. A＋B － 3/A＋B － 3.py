n = list(map(int, open(0).read().split()))
t = 0

for i in range(n[0]):
    print(n[i+t+1] + n[i+t+2])
    t += 1
