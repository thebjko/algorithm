i = int(input())

ls = []
result = 0

if i < 100:
    print(i)
else:
    for n in range(100, i):
        while n:
            ls.append(n%10)
            n //= 10
        if ls[0]-ls[1] == ls[1]-ls[2]:
            # try:
            #     if ls[1]-ls[2] == ls[2]-ls[3]:
            #         result += 1
            # except:
            result += 1
            # finally:
            ls = []
        else:
            ls = []

    print(result+99)

"""
숏코딩
print(sum(i<100or i//100*21+i==i//10*12for i in range(1,int(input())+1)))
숫자의 성질을 이용
i = 369 라고 할 때
3 * 21 + 369 == 63 + 369 == 432
36 * 12 == 432
비교연산자는 1로 카운트되는 True값을 반환
sum으로 더한 값을 출력
"""