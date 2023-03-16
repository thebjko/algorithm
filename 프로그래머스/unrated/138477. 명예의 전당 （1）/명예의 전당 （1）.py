def solution(k, score):
    answer, ls = [], []
    for i in score:
        ls.append(i)
        ls.sort(reverse=True)
        if len(ls) > k:
            ls.pop()
        answer.append(ls[-1])
            
    return answer


if __name__ == '__main__':
    test_cases =[
        [3, [10, 100, 20, 150, 1, 100, 200]],
        [4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]],
    ]

    for tc in test_cases:
        print(solution(*tc))