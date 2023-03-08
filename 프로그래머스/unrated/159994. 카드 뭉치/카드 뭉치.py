def solution(cards1, cards2, goal):
    indices = [0, 0]
    for word in goal:
        if indices[0] < len(cards1) and word == cards1[indices[0]]:
            indices[0] += 1
        elif indices[1] < len(cards2) and word == cards2[indices[1]]:
            indices[1] += 1
        else:
            answer = 'No'
            break
    else:
        answer = 'Yes'

    return answer