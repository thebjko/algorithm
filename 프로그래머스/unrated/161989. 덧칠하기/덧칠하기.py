def solution(n, m, section):
    cnt, adjusted_index, l = 0, 0, len(section)
    for i in range(l):
        i = adjusted_index
        if i+1 == l:
            cnt += 1
            break
        for j in range(i+1, l):
            if section[j] - section[i] < m:
                adjusted_index = j
                continue
            else:
                cnt += 1
                adjusted_index = j
                break
    
    return cnt