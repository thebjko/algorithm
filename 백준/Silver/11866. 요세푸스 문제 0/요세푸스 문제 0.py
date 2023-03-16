N, K = map(int, input().split())

s = set()
interval, index, cnt = 1, 0, 0

ls = []
while cnt < N:
    if index in s:
        index = (index + 1) % N
        continue

    if not interval % K:
        ls.append(str(index+1))
        s.add(index)
        cnt += 1

    interval = (interval + 1) % K
    index = (index + 1) % N

print('<' + ', '.join(ls) + '>')