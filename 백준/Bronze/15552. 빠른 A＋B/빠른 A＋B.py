import sys
from operator import add

nums = open(0).readlines()
for i in nums[1:]:
    a,b=i.split()
    print(add(int(a),int(b)))
