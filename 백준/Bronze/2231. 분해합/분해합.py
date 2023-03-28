n = int(input())
result = int(1e6)
for i in range(n-1, max(n-9*len(str(n))-1, 0), -1):
    if i + sum(map(int, str(i))) == n:
        if i < result:
            result = i

print(result if result != int(1e6) else 0)