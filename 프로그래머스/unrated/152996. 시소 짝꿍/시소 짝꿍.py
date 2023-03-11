from collections import Counter, defaultdict

def solution(numbers):
    counter = Counter(numbers)
    r1 = defaultdict(list)
    r2 = defaultdict(set)

    for i in counter:
        for j in [i*2, i*3, i*4]:
            r1[i].append(j)
            r2[j].add(i)
    answer = 0
    for n in counter:
        for j in r1[n]:
            for x in r2[j]:
                if x != n:
                    answer += counter[n]*counter[x]

    answer //= 2
    for cnt in counter.values():
        answer += (cnt*~-cnt)//2

    return answer