from operator import itemgetter as ig


def timer(time: str) -> int:
    h, m = map(int, time.split(':'))
    return h * 60 + m


def solution(plans):
    answer, stack = [], []
    for plan in plans:
        plan[1], plan[2] = timer(plan[1]), int(plan[2])
    
    plans.sort(key=lambda ls: ls[1])
    
    t, idx = plans[0][1], 0
    while idx < len(plans):
        stack.append(plans[idx])
        if t < stack[-1][1]:
            t = stack[-1][1]

        while stack and stack[-1][2]:
            t += 1
            stack[-1][2] -= 1
            if not stack[-1][2]:
                answer.append(stack.pop())
            if idx+1 < len(plans) and t == plans[idx+1][1]:
                stack.append(plans[idx+1])
                idx += 1
        idx += 1
        
    return list(map(ig(0), answer))


if __name__ == '__main__':
    test_cases = [
        [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]],
        [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]],
        # bbb, aaa, ccc
        [["aaa", "12:00", "30"], ["bbb", "12:10", "30"], ["ccc", "14:00", "30"]],
        [['A', "12:00", "30"], ['B', "12:10", "20"], ['C', "15:00", "40"], ['D', "15:10", "30"]],
    ]
    for tc in test_cases:
        print(solution(tc))