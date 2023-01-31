words = []
for word in open(0):
    words += [word.strip() + " " * (16 - len(word))]

words = list(map(list, zip(*words)))
for x in words:
    print(''.join(x).replace(" ", ""), end="")