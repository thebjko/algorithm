def mine(board):
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

def isWin(board, x, y):
    leftY, rightY = (y - 1) % 3, (y + 1) % 3
    if board[x][y] == board[x][leftY] == board[x][rightY]:
        return True

    upX, downX = (x - 1) % 3, (x + 1) % 3
    if board[x][y] == board[upX][y] == board[downX][y]:
        return True

    if (board[x][y] == board[upX][leftY] == board[downX][rightY]) or (board[x][y] == board[upX][rightY] == board[downX][leftY]):
        return True

    return False

# 출처 : https://yuni0822.tistory.com/334
def yuni(board):
    n = len(board)

    oList, xList = [], []
    for x in range(n):
        for y in range(n):
            if board[x][y] == 'O':
                oList.append((x, y))
            elif board[x][y] == 'X':
                xList.append((x, y))

    if len(oList) < len(xList) or len(oList) >= (len(xList) + 2):
        return 0

    for x, y in oList:
        if isWin(board, x, y) and len(xList) != (len(oList) - 1):
            return 0

    for x, y in xList:
        if isWin(board, x, y) and len(xList) != len(oList):
            return 0

    return 1

if __name__ == '__main__':
    from itertools import product
    p = list(map(''.join, product(['.', 'O', 'X'], repeat=3)))
    boards = list(product(p, repeat=3))

    # boards = [['XXO', 'XOO', 'OOX']]

    def pprint(arg):
        for i in arg:
            print(i)

    for i in boards:
        m = mine(i)
        y = yuni(i)
        if m^y:
            print(f'mine {m}, yuni {y}')
            pprint(i)
        # if mine(i) and not yuni(i):
        #     print('mine 1, yuni 0')
        #     pprint(i)
        # if not mine(i) and yuni(i):
        #     print('mine 0, yuni 1')
        #     pprint(i)