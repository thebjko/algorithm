# PyPy3로 제출시 맞았습니다!!
# 파이썬은 왜 안될까?
# import time

T = int(input())
# start_time = time.time()
n = 1

denominator = [[1]]
numerator = [[1]]

flag = 1

while True:
    if T > n:
        T -= n
        n += 1
        
        ls = [*range(1, n + 1)]
        numerator.append(ls[::flag])
        flag *= -1
        denominator.append(ls[::flag])

    else:
        print(f"{denominator[n - 1][n - T]}/{numerator[n - 1][n - T]}")
        # end_time = time.time()
        # print(end_time - start_time)
        break

