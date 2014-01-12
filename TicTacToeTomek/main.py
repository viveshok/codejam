
def horizontal_win(player, board):
    for row in range(4):
        if set(board[row]) <= {player, 'T'}:
            return True
    return False

def vertical_win(player, board):
    for col in range(4):
        if {board[0][col], board[1][col], board[2][col], board[3][col]} <= {player, 'T'}:
            return True
    return False
        
def diagonal_win(player, boart):
    if {board[0][0], board[1][1], board[2][2], board[3][3]} <= {player, 'T'}:
        return True
    elif {board[0][3], board[1][2], board[2][1], board[3][0]} <= {player, 'T'}:
        return True
    else:
        return False

def draw(board):
    board_str = ''.join([str(x) for x in board])
    return '.' not in board_str

if __name__ == "__main__":

    finput = open("/home/alexandre/codejam/TicTacToeTomek/A-large.in", 'r')
    foutput = open("/home/alexandre/codejam/TicTacToeTomek/A-large.out", 'w')

    num_cases = int(finput.readline())

    for case in range(num_cases):

        # Read board
        board = [['.','.','.','.'],['.','.','.','.'],['.','.','.','.'],['.','.','.','.']]
        for i in range(4):
            row = finput.readline()
            for j, col in enumerate(row[:-1]):
                board[i][j] = col
        finput.readline()

        for player in "XO":
            if horizontal_win(player, board):
                foutput.write("Case #" + str(case+1) + ": " + str(player) + " won\n")
                break
            if vertical_win(player, board):
                foutput.write("Case #" + str(case+1) + ": " + str(player) + " won\n")
                break
            if diagonal_win(player, board):
                foutput.write("Case #" + str(case+1) + ": " + str(player) + " won\n")
                break
            if player == 'O' and draw(board):
                foutput.write("Case #" + str(case+1) + ": Draw\n")
                break
            if player == 'O':
                foutput.write("Case #" + str(case+1) + ": Game has not completed\n")
                break

    finput.close()
    foutput.close()

