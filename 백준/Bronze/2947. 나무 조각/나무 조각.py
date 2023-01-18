ls = list(open(0).read().split())

while ls != ['1', '2', '3', '4', '5']:
    for i in range(len(ls)):
        try:
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                print(*ls)
            else:
                continue
        except:
            continue
        