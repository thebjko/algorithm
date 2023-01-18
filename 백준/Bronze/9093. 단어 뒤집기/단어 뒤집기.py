_, *a = open(0)

for i in a:
    for j in i.split():
        print(j[::-1], end=' ')
    print('')