import re, time
from itertools import product

start_time = time.time()

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

end_time = time.time()

print(end_time - start_time)




start_time = time.time()
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
end_time = time.time()

print(end_time - start_time)

