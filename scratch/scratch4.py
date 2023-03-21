_, *ls = open('input.txt')
songs = list(map(lambda x: x.rstrip(), ls[::2]))
ups_or_downs = list(map(lambda x: x.rstrip(), ls[1::2]))

ups, downs, sames = set(), set(), set()
for i, j in enumerate(ups_or_downs):
    if 'UP' in j:
        ups.add(songs[i])
    elif 'DOWN' in j:
        downs.add(songs[i])
    else:
        sames.add(songs[i])

original = list(downs) + list(ups)
for i, j in enumerate(songs):
    if j in sames:
        original.insert(i, j)

# index = 0
# for index in range(len(original) - 1):
#     idx = index + 1
#     while original[index] in downs and idx < len(original) and original[idx] not in ups:
#         idx += 1
#     original[index], original[idx] = original[idx], original[index]

print(*original)