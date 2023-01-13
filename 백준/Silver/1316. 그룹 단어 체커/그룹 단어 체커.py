T = int(input())

n = []
m = 0
for i in range(T):
    word = input()
    for index, char in enumerate(word):
        if word.count(char) * char in word:
            n.append(char)
        else:
            n = []
            break
        if ''.join(n) == word:
            m += 1
            n = []

print(m)
           