def solution(keymap, targets):
    answer = []
    for s in targets:
        cnt = 0
        for char in s:
            stroke = set(map(lambda x: x.find(char), keymap))
            if stroke == {-1}:
                cnt = -1
                break
            stroke.discard(-1)
            cnt += min(stroke)+1
        answer.append(cnt)
    
    return answer