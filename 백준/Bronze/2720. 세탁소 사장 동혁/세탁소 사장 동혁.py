for i in range(int(input())):
    change = int(input())
    coins = [25, 10, 5, 1]
    changes = []
    for i in coins:
        changes += [change //i]
        change %= i
    print(*changes)