import sys
sys.stdin = open('input.txt')

# # ls = list(input().upper())
# ls = list('a'*1000000)
# sls = []

# for i, j in enumerate(ls):
#     sls.append(ls.count(ls[i]))

# lsls = set(zip(ls, sls))

# x = 0
# y = ''

# for i, j in lsls:
#     if j == x:
#         print('?')
#         exit()
#     elif j > x:
#         x = j
#         y = i

# print(y)
    

ls = list(input().upper())
# ls = list('A'*500_000 + 'B'*500_000)
alphabet = [*map(chr, range(65, 91))]
cnt = []

for i in alphabet:
    cnt.append(ls.count(i))

x = max(cnt)
if cnt.count(x) > 1:
    print('?')
else:
    print(ls[cnt.index(x)])


# n = -1
# for i in alphabet:
#     d[i] = ls.count(i)
#     if ls.count(i) > n:
#         n = ls.count(i)

# m = 0
# for i, j in d.items():
#     print(i)
#     if j == n:
#         d.pop(i)
#         m += 1
    
# if m > 1:
#     print('?')
# else:
#     # Python: Get Dictionary Key with the Max Value (4 Ways)
#     # https://datagy.io/python-get-dictionary-key-with-max-value/
#     print(max(d, key=d.get))


    
