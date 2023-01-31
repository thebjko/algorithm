words = []
for word in open(0):
    words += [word.strip()]

m = max(map(len, words))
for idx, word in enumerate(words):
    words[idx] += " " * (m - len(word))

words = list(map(list, zip(*words)))
for word in words:
    print(''.join(word).replace(" ", ""), end="")