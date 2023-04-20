import sys

input = sys.stdin.readline

N, M = map(int, input().split())
names_to_indices = {}
indices_to_names = [''] * (N+1)
for i in range(1, N+1):
    name = input().rstrip()
    names_to_indices[name] = i
    indices_to_names[i] = name

for _ in range(M):
    x = input().rstrip()
    if x in names_to_indices:
        print(names_to_indices[x])
    else:
        print(indices_to_names[int(x)])