n, m, *ls = map(int, open(0).read().split())

def f(ls: list) -> int:
    min_ls = min(ls)
    max_ls = max(ls)
    n = len(ls)
    s = sum(ls)-n*min_ls

    if s <= m:
        return min_ls-(m-s+n-1)//n
    else:
        l,r = min_ls, max_ls
        while l <= r:
            mid = (l+r)//2
            ls_to_pass = []
            cut = 0
            for i, j in enumerate(ls):
                if j-mid > 0:
                    cut += j-mid
                    ls_to_pass.append(j)
            
            if cut > m:
                ls.clear()
                return f(ls_to_pass)
            else:
                r = mid-1


print(f(ls))