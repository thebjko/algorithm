import re
from itertools import product

hour = list(range(int(input()) + 1))
min = list(range(60))
sec = list(range(60))

str_hour = list(map(str, hour))
str_min = list(map(str, min))
str_sec = list(map(str, sec))
prod = product(str_hour, str_min, str_sec)

n = 0
for hour, min, sec in prod:
    if re.search('3', hour) or re.search('3', min) or re.search('3', sec):
        n += 1

print(n)