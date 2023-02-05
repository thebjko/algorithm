from math import sqrt, ceil

_, *ls = map(int, open(0).read().split())

def prime(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    for i in range(3, ceil(sqrt(n + 1)), 2):
        if sieve[i]:
            # https://math.stackexchange.com/questions/2464224/time-complexity-of-the-ceiling
            sieve[i*i::2*i] = [False] * ceil(((n + 1) - (i * i)) / (2 * i))

    return [2] + [j for j in range(3, n + 1, 2) if sieve[j]]

def search(prime_list: list[int], n: int) -> int:
    l, r = 0, len(prime_list) - 1
    m = 0
    while l <= r:
        m = (l + r) // 2

        if prime_list[m] > n:
            r = m - 1
        
        elif prime_list[m] < n:
            l = m + 1

    return m

for n in ls:
    prime_list = prime(n)
    n //= 2

    if n in (s := set(prime_list)):
        print(f"{n} " * 2)
    
    else:
        m = search(prime_list, n)
        n *= 2
        while True:
            if (k := n - prime_list[m]) in s:
                print(*sorted([k, prime_list[m]]))
                break
            else:
                m += 1