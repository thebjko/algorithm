_, *a = open(0).read().split()
print(len(a) - len(set(a)))