from collections import defaultdict

# 1번, 17번
def solution(today, terms, privacies):
    terms_dict = defaultdict(int)
    for idx, term in enumerate(terms):
        key, val = term.split()
        terms_dict[key] = int(val)

    result = []
    for idx, val in enumerate(privacies):
        date, term = val.split()
        date = list(map(int, date.split('.')))
        date[1] += terms_dict[term]
        date[0] += (date[1] - 1) // 12
        date[1] -= ((date[1] - 1) // 12) * 12
        date = '.'.join(map(lambda x: str(x).zfill(2), date))
        if date <= today:
            result.append(idx+1)
        
    return sorted(result)