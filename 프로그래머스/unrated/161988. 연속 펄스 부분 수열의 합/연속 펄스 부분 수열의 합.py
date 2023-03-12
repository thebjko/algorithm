def solution(sequence):
    result = []
    for flag in [1, -1]:
        dp = []
        for i in sequence:
            dp.append(i*flag)
            flag *= -1
        
        for idx in range(1, len(dp)):
            dp[idx] = max(dp[idx-1]+dp[idx], dp[idx])
        
        result.append(max(dp))

    return max(result)