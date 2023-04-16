def solution(r1, r2):
    answer = 0
    for a in range(-r2, r2+1):
        b = (r2**2-a**2)**.5
        answer += 2*int(b)+1

    for a in range(-r1, r1+1):
        b = (r1**2-a**2)**.5
        answer -= 2*int(b)+1
        if b - int(b) == 0:
            answer += 1 if b == 0 else 2

    return answer