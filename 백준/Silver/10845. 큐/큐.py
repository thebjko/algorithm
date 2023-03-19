q = []
for i in [*open(0)][1:]:
    if 'push' in i:
        q.append(i[5:-1])
    elif 'pop' in i:
        print(q.pop(0) if q else -1)
    elif 'size' in i:
        print(len(q))
    elif 'empty' in i:
        print(0 if q else 1)
    elif 'front' in i:
        print(q[0] if q else -1)
    else:
        print(q[-1] if q else -1)