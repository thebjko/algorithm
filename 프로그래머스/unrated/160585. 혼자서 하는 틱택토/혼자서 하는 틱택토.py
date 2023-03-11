def solution(board):
    # 1. X가 더 많거나 O가 X보다 2이상 크면 0 리턴
    O, X = 0, 0
    for i in range(3):
        for j in range(3):
            if board[j][i] == 'O':
                O += 1
            elif board[j][i] == 'X':
                X += 1

    if not (0 <= O-X <= 1):
        return 0

    # 2. O in a row(or col) and X in a row(or col)
    o_row = False
    x_row = False
    for i in board:
        if i == 'OOO':
            o_row = True
        if i == 'XXX':
            x_row = True

    if o_row and x_row:
        return 0

    transposed = list(map(''.join, zip(*map(list, board))))

    o_col = False
    x_col = False
    for i in transposed:
        if i == 'OOO':
            o_col = True
        if i == 'XXX':
            x_col = True

    if o_col and x_col:
        return 0

    # 3. O in diagonals
    adjusted_board = []
    for i in range(3):
        adjusted_board.append(' '*i + board[i] + ' '*(2-i))

    adjusted_transposed = list(map(''.join, zip(*map(list, adjusted_board))))
    o_diag_1 = False
    x_diag_1 = False
    if adjusted_transposed[2] == 'OOO':
        o_diag_1 = True
    if adjusted_transposed[2] == 'XXX':
        x_diag_1 = True

    adjusted_board = []
    for i in range(3):
        adjusted_board.append(' '*(2-i) + board[i] + ' '*i)

    adjusted_transposed = list(map(''.join, zip(*map(list, adjusted_board))))
    o_diag_2 = False
    x_diag_2 = False
    if adjusted_transposed[2] == 'OOO':
        o_diag_2 = True
    if adjusted_transposed[2] == 'XXX':
        x_diag_2 = True

    # 1-1. X가 이겼을 때는 무조건 숫자가 같아야 한다.
    if x_col or x_row or x_diag_1 or x_diag_2:
        if O-X != 0:
            return 0

    # 1-2. O가 이겼을 때는 차이가 1이어야한다.
    if o_col or o_row or o_diag_1 or o_diag_2:
        if O-X != 1:
            return 0

    return 1