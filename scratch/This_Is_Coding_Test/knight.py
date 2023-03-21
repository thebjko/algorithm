row, column = input()

row = ord(row) - ord('a') + 1
column = int(column)

steps = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

result = 0
for x, y in steps:
    next_row = row + x
    next_col = column + y
    
    if next_row > 0 and next_row < 9 and next_col > 0 and next_col < 9:
        result += 1

print(result)