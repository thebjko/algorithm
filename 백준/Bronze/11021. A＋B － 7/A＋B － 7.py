import sys

nums = sys.stdin.readlines()
for i, j in enumerate(nums[1:]):
    print(f'Case #{i+1}:', sum(map(int, j.split())))
