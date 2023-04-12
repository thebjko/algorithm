def solution(seq, k):
    partial_sum = 0
    idx = 0
    answer = []
    for i, j in enumerate(seq):
        partial_sum += j
        while partial_sum > k:
            partial_sum -= seq[idx]
            idx += 1
        if partial_sum == k:
            answer.append((i-idx, [idx, i]))
    answer.sort()
    return answer[0][1]