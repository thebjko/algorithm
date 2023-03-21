from collections import Counter

a, b = map(int, input().split())

def prime(n: int) -> list[int]:
    sieve: list = [True] * (n+1)
    for i in range(3, int(n**.5) + 1, 2):
        if sieve[i]:
            sieve[2*i::i*i] = [False] * ((n - 2*i + i*i) // (i*i))

    return [2] + [i for i in range(3, n+1, 2) if sieve[i]]

ls_a, ls_b = [], []
for n in prime(max(a, b)):
    while a % n == 0:
        ls_a.append(n)
        a //= n
    while b % n == 0:
        ls_b.append(n)
        b //= n

counter_a, counter_b = Counter(ls_a), Counter(ls_b)

lcd, gcm = 1, 1
s = set(counter_a.keys()).union(set(counter_b.keys()))
for n in s:
    lcd *= n**min(counter_a[n], counter_b[n])
    gcm *= n**max(counter_a[n], counter_b[n])

print(lcd, gcm)