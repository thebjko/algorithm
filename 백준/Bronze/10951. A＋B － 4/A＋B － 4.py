for line in open(0).readlines():
    ls = list(map(int, line.split()))
    print(sum(ls))