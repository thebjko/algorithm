ls = list(input().upper())
# ls = list('A'*500_000 + 'B'*500_000)
# alphabet = [*map(chr, range(65, 91))]
alphabet = list(set(ls))
cnt = []

for i in alphabet:
    cnt.append(ls.count(i))

x = max(cnt)
if cnt.count(x) > 1:
    print('?')
else:
    print(alphabet[cnt.index(x)])

"""
Note:
s = input().upper()
# c = s.count
*_,a,b = v = sorted({*s, '?'}, key=s.count)   # <class 'list'>
print(v[-(s.count(a) < s.count(b))])
"""