from itertools import product

time_table = {val: idx for idx, val in enumerate(map(':'.join, product(
    [str(i).zfill(2) for i in range(0, 24)], [str(i).zfill(2) for i in range(0, 60)]
)))}


def solution(book_time):
    reservation_table = [0] * 3600
    for start, end in book_time:
        for i in range(time_table[start], time_table[end] + 10):
            reservation_table[i] += 1
    return max(reservation_table)