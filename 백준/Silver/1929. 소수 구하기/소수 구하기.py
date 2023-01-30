m, n = map(int, open(0).read().split())

ls = [2, *range(3, n + 1, 2)]
s = set(ls)

i = 0
while True:
    if i > n ** .5 / 2:
        break
    try:
        entry = ls[i]
        if entry == 2:
            continue   # try 블록에서 continue를 하더라도 finally 블록이 실행된다
        else:
            s -= {j for j in range(2 * entry, n + 1, entry)}
            ls = sorted(list(s))
            s = set(ls)
    except:
        pass
    finally:
        i += 1

print(*sorted([i for i in ls if i >= m]), sep="\n")