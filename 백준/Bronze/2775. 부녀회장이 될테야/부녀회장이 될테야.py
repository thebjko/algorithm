from math import factorial

_, *a = map(int, open(0).read().split())

for k, n in zip(a[::2], a[1::2]):
    """
    k += 1에 관하여:
    예를 들어 k 입력값이 5일 때(5층) 0층부터 시작하므로 
    6차(k + 1)의 이항계수(1 6 15 20 15 6 1)를 사용하여 증가시킨다.
    """
    k += 1   
    ls = [1.0]

    # 파스칼의 삼각형
    for i in range(1, k + 1):
        ls.append(factorial(k)/(factorial(i)*factorial(k-i)))

    # 각 원소의 다음 원소는 자신의 증가율이므로 각 원소의 다음 원소를 더해주고 ls에 반영한다.
    # 마지막 원소의 증가율은 0이므로 IndexError에서 pass.
    # 1호(1명)에서부터 n - 1번 증가하면 ls[0] == n호의 입주자 수가 된다.
    for _ in range(n - 1):
        for i, _ in enumerate(ls):
            try:
                ls[i] += ls[i + 1]
            except IndexError:
                pass

    print(int(ls[0]))
