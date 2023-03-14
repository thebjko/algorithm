from collections import defaultdict
from itertools import product

dates_dict = {
    '.'.join(date): idx for idx, date in enumerate(
        product(
            [str(l) for l in range(2000, 2032)],
            [str(m).zfill(2) for m in range(1, 13)],
            [str(n).zfill(2) for n in range(1, 29)]
        )
    )
}

# 10, 12, 15, 18, 20
def solution(today, terms, privacies):
    terms_dict = defaultdict(int)
    for term in terms:
        key, val = term.split()
        terms_dict[key] = int(val)

    privacies_dict = defaultdict(list)
    for idx, term in enumerate(privacies):
        privacies_dict[term].append(idx+1)

    idx_today = dates_dict[today]    
    
    answer = []
    for prv in set(privacies):
        date, term = prv.split()
        if dates_dict[date] + 28 * terms_dict[term] <= idx_today:
            answer += privacies_dict[prv]

    return sorted(answer)

if __name__ == '__main__':
    cases = [
        ["2022.12.08", ["A 6"], ["2022.06.08 A"]],
        ["2021.12.08", ["A 18"], ["2020.06.08 A"]],
    ]

    for c in cases:
        print(solution(*c))