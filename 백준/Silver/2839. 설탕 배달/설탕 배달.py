N = int(input())

div, mod = divmod(N, 5)
while div >= 0:
    if mod % 3 == 0:
        div += mod // 3
        print(div)
        exit()
    elif mod % 3 != 0:
        div -= 1
        mod += 5
    
print(-1)