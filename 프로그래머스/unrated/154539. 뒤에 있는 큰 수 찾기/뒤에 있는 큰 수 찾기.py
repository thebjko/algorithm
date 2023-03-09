def solution(numbers):
    len_nums = len(numbers)
    answers = [-1] * len_nums
    stack = []
    for i in enumerate(numbers):
        while stack:
            if stack[-1][1] >= i[1]:
                break
            answers[stack.pop()[0]] = i[1]
        stack.append(i)
    
    return answers