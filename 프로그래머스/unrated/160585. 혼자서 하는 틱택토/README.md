# [unrated] 혼자서 하는 틱택토 - 160585 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/160585) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>틱택토는 두 사람이 하는 게임으로 처음에 3x3의 빈칸으로 이루어진 게임판에 선공이 "O", 후공이 "X"를 번갈아가면서 빈칸에 표시하는 게임입니다. 가로, 세로, 대각선으로 3개가 같은 표시가 만들어지면 같은 표시를 만든 사람이 승리하고 게임이 종료되며 9칸이 모두 차서 더 이상 표시를 할 수 없는 경우에는 무승부로 게임이 종료됩니다.</p>

<p>할 일이 없어 한가한 머쓱이는 두 사람이 하는 게임인 틱택토를 다음과 같이 혼자서 하려고 합니다.</p>

<ul>
<li>혼자서 선공과 후공을 둘 다 맡는다.</li>
<li>틱택토 게임을 시작한 후 "O"와 "X"를 혼자서 번갈아 가면서 표시를 하면서 진행한다.</li>
</ul>

<p>틱택토는 단순한 규칙으로 게임이 금방 끝나기에 머쓱이는 한 게임이 종료되면 다시 3x3 빈칸을 그린 뒤 다시 게임을 반복했습니다. 그렇게 틱택토 수 십 판을 했더니 머쓱이는 게임 도중에 다음과 같이 규칙을 어기는 실수를 했을 수도 있습니다.</p>

<ul>
<li>"O"를 표시할 차례인데 "X"를 표시하거나 반대로 "X"를 표시할 차례인데 "O"를 표시한다.</li>
<li>선공이나 후공이 승리해서 게임이 종료되었음에도 그 게임을 진행한다.</li>
</ul>

<p>게임 도중 게임판을 본 어느 순간 머쓱이는 본인이 실수를 했는지 의문이 생겼습니다. 혼자서 틱택토를 했기에 게임하는 과정을 지켜본 사람이 없어 이를 알 수는 없습니다. 그러나 게임판만 봤을 때 실제로 틱택토 규칙을 지켜서 진행했을 때 나올 수 있는 상황인지는 판단할 수 있을 것 같고 문제가 없다면 게임을 이어서 하려고 합니다.</p>

<p>머쓱이가 혼자서 게임을 진행하다 의문이 생긴 틱택토 게임판의 정보를 담고 있는 문자열 배열 <code>board</code>가 매개변수로 주어질 때, 이 게임판이 규칙을 지켜서 틱택토를 진행했을 때 나올 수 있는 게임 상황이면 1을 아니라면 0을 return 하는 solution 함수를 작성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li><code>board</code>의 길이 = <code>board[i]</code>의 길이 = 3

<ul>
<li><code>board</code>의 원소는 모두 "O", "X", "."으로만 이루어져 있습니다.</li>
</ul></li>
<li><code>board[i][j]</code>는 <code>i</code> + 1행 <code>j</code> + 1열에 해당하는 칸의 상태를 나타냅니다.

<ul>
<li>"."은 빈칸을, "O"와 "X"는 해당 문자로 칸이 표시되어 있다는 의미입니다.</li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>board</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>["O.X", ".O.", "..X"]</td>
<td>1</td>
</tr>
<tr>
<td>["OOO", "...", "XXX"]</td>
<td>0</td>
</tr>
<tr>
<td>["...", ".X.", "..."]</td>
<td>0</td>
</tr>
<tr>
<td>["...", "...", "..."]</td>
<td>1</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li><p>예제 1번의 게임판은 다음과 같습니다.</p>
<div class="highlight"><pre class="codehilite"><code>O.X
.O.
..X
</code></pre></div>
<p>선공 후공이 번갈아가면서 다음과 같이 놓았을 때 이러한 게임판이 나올 수 있습니다.</p>

<ul>
<li>1행 1열 → 1행 3열 → 2행 2열 → 3행 3열</li>
<li>1행 1열 → 3행 3열 → 2행 2열 → 1행 3열</li>
<li>2행 2열 → 1행 3열 → 1행 1열 → 3행 3열</li>
<li>2행 2열 → 3행 3열 → 1행 1열 → 1행 3열</li>
</ul>

<p>물론 위와 다르게 머쓱이가 2행 2열에 <code>O</code>, 3행 3열에 <code>X</code>, 1행 3열에 <code>X</code>, 1행 1열에 <code>O</code> 순서로 표시를 해서 실수를 했을 가능성도 있지만 "<strong>실수를 했을 가능성이 있는가</strong>"를 묻는 게 아닌 "이 게임판이 <strong>규칙을 지켜서 진행한 틱택토에서 나올 수 있는 상황인가</strong>"를 묻는 문제라는 것에 유의해주세요. 따라서 1을 return 합니다.</p></li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><p>예제 2번의 게임판은 다음과 같습니다.</p>
<div class="highlight"><pre class="codehilite"><code>OOO
...
XXX
</code></pre></div>
<p>규칙을 지켜서 진행한 틱택토라면 선공과 후공이 번갈아가면서 각각 1행, 3행 중 두 칸씩에 표시를 한 뒤 5번째 차례에 선공이 1행에 가로로 3개의 <code>O</code>를 완성했을 때 종료되므로 적어도 머쓱이가 게임이 종료된 후에도 계속 진행하는 실수를 했다는 것을 추론해 볼 수 있고, 정상적인 틱택토에서는 이러한 상황이 나올 수 없습니다. 따라서 0을 return 합니다.</p></li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>예제 3번은 2행 2열에만 <code>X</code>가 표시가 되어있습니다. 선공 <code>O</code> 표시가 없이 <code>X</code>만 있으므로 머쓱이가 <code>O</code>를 표시해야 할 때 <code>X</code>를 표시하는 실수를 했다는 것을 추론해 볼 수 있고, 규칙을 지켜서 진행했을 때는 이러한 상황이 나올 수 없습니다. 따라서 0을 return 합니다.</li>
</ul>

<p>입출력 예 #4</p>

<ul>
<li>예제 4번은 빈 3x3 게임판입니다. 선공이 아직 빈칸에 표시하기 전에 이러한 상황이 나올 수 있습니다. 따라서 1을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 다른 코드와 비교하며 전수조사 하기 위해 사용한 코드
```python
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


# Jacky Chai Chen Long 님의 코드
# Check if there is a winning row, column, or diagonal
def check_win(player, board):
    # Check rows
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True

    # Check columns
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def solution(board):
    num_x = sum(row.count('X') for row in board)
    num_o = sum(row.count('O') for row in board)

    if num_x - num_o > 0 or abs(num_x - num_o) > 1:
        return 0

    elif (check_win('O', board) and num_x != num_o - 1) or (check_win('X', board) and num_x != num_o):
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
        y = solution(i)
        if m^y:
            print(f'mine {m}, yuni {y}')
            pprint(i)

```
> 내것도 맞더라