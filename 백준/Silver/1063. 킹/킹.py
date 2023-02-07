import sys
from itertools import product

input = sys.stdin.readline

king, stone, n = input().split()

king = tuple(map(ord, king))
stone = tuple(map(ord, stone))
n = int(n)

d = ["RT", "RB", "R", "LT",  "LB", "L", "T", "B"]
prod = list(product([1,-1,0], repeat=2))
d = dict(zip(d, prod[:-1]))

def move(current_position: tuple[int, int], dir: tuple[int, int]) -> tuple[int, int]:    
    (x, y) = current_position
    
    x += dir[0]
    y += dir[1]

    return (x, y)
    
for _ in range(n):
    dir = d.get(input().strip())
    x, y = move(king, dir)
    (a, b) = (0, 0)

    if (x, y) == stone:
        a, b = move(stone, dir)
    else:
        (a, b) = stone

    if x < 65 or a < 65 or x > 72 or a > 72 or y < 49 or b < 49 or y > 56 or b > 56:
        continue

    king = x, y
    stone = a, b
    
print("".join(map(chr, king)))
print("".join(map(chr, stone)))