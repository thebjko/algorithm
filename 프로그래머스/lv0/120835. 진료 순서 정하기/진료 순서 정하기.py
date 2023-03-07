def solution(emergency: list):
    l = len(emergency)
    answer = [1] * l
    for i in range(l):
        for j in range(l):
            if emergency[i] < emergency[j]:
                answer[i] += 1
    return answer