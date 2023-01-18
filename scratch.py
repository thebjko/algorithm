# import time

T = int(input())
# start_time = time.time()
n = 1

flag = 1
numerator = [1]
denominator = [1]
while T > n:
    T -= n
    n += 1
    
    ls = [*range(1, n+1)]
    numerator = ls[::flag]
    flag *= -1
    denominator = ls[::flag]
    print(denominator, numerator, n-T)

print(f"{denominator[n - T]}/{numerator[n - T]}")
# end_time = time.time()
# print(end_time - start_time)


