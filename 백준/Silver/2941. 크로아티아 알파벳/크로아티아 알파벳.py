cr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
n = len(s)
for i in cr:
    n -= s.count(i)

print(n)

"""
숏코딩
import re
print(len(re.sub('dz=|[ln]j|\w\W','Z',input())))

한 문자로 변환해서 계산
"""