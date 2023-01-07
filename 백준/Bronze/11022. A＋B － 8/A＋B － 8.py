import sys

nums = sys.stdin.readlines()
for i, j in enumerate(nums[1:], 1):
    a, b = map(int, j.split())
    print(f'Case #{i}: {a} + {b} = {a + b}')
    