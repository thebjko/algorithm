employees = {}
for i in range(int(input())):
    name, status = input().split()
    employees[name] = status

(ls := sorted([i for i, j in employees.items() if j == 'enter'])).reverse()
print(*ls)