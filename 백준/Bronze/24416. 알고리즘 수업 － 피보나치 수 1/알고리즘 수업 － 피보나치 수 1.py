ls = [0, 1, 1]
for i in range(3, int(input())+1):
    ls.append(ls[i-1]+ls[i-2])
print(ls[-1], len(ls)-3)