from collections import Counter
n, *ls = map(int, open(0).read().split())
ls, counter = sorted(ls), Counter(ls)
most_common = counter.most_common(1)[0][1]
filtered = sorted(filter(lambda x: counter[x] == most_common, counter))

print(round(sum(ls)/n), ls[n//2], filtered[len(filtered)>1], ls[-1]-ls[0])