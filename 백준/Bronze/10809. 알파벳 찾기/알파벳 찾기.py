s = input()

for i in range(97, 123):
    if chr(i) in s:
        print(s.index(chr(i)), end=' ')
    else:
        print(-1, end=' ')
        
"""print(*map(input().find,map(chr,range(97,123))))"""
