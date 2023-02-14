_, *ls = map(int, open(0))

apartment = [[0] * 15 for _ in " "*15]
# 다운업: 메모리 약 31MB, 시간 60ms
# for k in range(15):
#     for n in range(1, 15):
#         if k == 0:
#             apartment[k][n] = n
#         else:
#             apartment[k][n] = apartment[k-1][n] + apartment[k][n-1]

# for k, n in zip(ls[::2], ls[1::2]):
#     print(apartment[k][n])


# 탑다운
def f(k, n):
    if apartment[k][n] == 0:
        if k == 0:
            apartment[k][n] = n
            return apartment[k][n]
            
        x = 0
        for i in range(n+1):
            x += f(k - 1, i)

        apartment[k][n] = x

    return apartment[k][n]
    
for k, n in zip(ls[::2], ls[1::2]):
    print(f(k, n))
