def solution(num, total):
    answer = []
    a = num//2
    answer += [*range(total//num-a, total//num+a+1)]
    if not num%2:
        if sum(answer[1:]) == total:
            answer.pop(0)
        else:
            answer.pop()

    return answer