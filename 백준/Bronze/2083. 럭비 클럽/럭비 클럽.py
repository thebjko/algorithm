*ls, = open(0)
for i in ls[:-1]:
    a,b,c = i.split()
    if int(b) > 17 or int(c) >= 80:
        print(f'{a} Senior')
    else:
        print(f'{a} Junior')