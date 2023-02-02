N, *ls = map(int, open(0).read().split())
# 원소끼리의 차 구하기
d = [ls[i + 1] - ls[i] for i in range(N - 1)]

# 초기값 설정
bottom = ls[0]
apex = 0
result = [0]   # 음수만 저장될 경우를 대비

for idx, diff in enumerate(d):
    h = ls[idx + 1]

    if diff > 0:
        apex = h

    else:
        result.append(apex - bottom)
        bottom = h
        apex = 0

# 종료시 마지막으로 저장된 apex와 bottom을 가지고 연산 수행 후 result에 append
result.append(apex - bottom)
print(max(result))