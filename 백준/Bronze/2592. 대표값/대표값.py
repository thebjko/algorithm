from collections import Counter
ls = list(map(int, open(0).read().split()))
most_common = Counter(ls).most_common(1)[0][0]
print(int(sum(ls)/10), most_common)