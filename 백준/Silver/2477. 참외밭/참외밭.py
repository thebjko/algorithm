n, *ls = map(int, open(0).read().split())

distance = ls[1::2]

big_side_1 = sum(distance[::2]) / 2
big_side_2 = sum(distance[1::2]) / 2
small_side_1 = distance[(distance.index(big_side_1) + 3) % 6]
small_side_2 = distance[(distance.index(big_side_2) + 3) % 6]

big = big_side_1 * big_side_2
small = small_side_1 * small_side_2

A = big - small
mellons = n * A

print(int(mellons))