nums = input()
nums = nums.split(sep=' ')

A = int(nums[0])
B = int(nums[1])
C = int(nums[2])

print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)