N = int(input())
dp = [0]+[*range(3*10**6)]
for i in range(0, N):
    dp[i*2] = min(dp[i]+1, dp[i*2])
    dp[i*3] = min(dp[i]+1, dp[i*3])
    dp[i+1] = min(dp[i+1], dp[i]+1)

print(dp[N])