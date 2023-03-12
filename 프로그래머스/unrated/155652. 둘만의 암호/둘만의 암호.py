def solution(s, skip, index):
    skip = set(map(ord, skip))
    answer = ''
    for i in map(ord, s):
        tmp = index
        while tmp:
            i += 1
            if (i - 97)%26+97 in skip:
                continue
            tmp -= 1
        answer += chr((i-97)%26+97)

    return answer