word = open(0).read().strip()
ln = len(word)

beginning = []
for i in range(1, ln - 1):
    beginning.append(word[:i][::-1])

middle = []
i = len(first := min(beginning))
for j in range(i + 1, ln):
    middle.append(word[i:j][::-1])

j = len(mid := min(middle)) + i
print(first + mid + word[j:][::-1])