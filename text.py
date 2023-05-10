ROWS = 6
COLS = 7

board = [[" " for i in range(COLS)] for j in range(ROWS)]
lowest = [0 for i in range(COLS)]
turn = 0


def printBoard():
    print("-"*(2*COLS+1))
    for i in range(ROWS-1, -1, -1):
        for j in range(0, COLS):
            print("|" + str(board[i][j]), end="")
        print("|")
        print("-"*(2*COLS+1))
    print()


def checkWinner(x, y):
    for i in range(-3, 1):
        # rows
        if (0 <= x+i and x+i < ROWS):
            if (board[y][x+i] == board[y][x+i+1] == board[y][x+i+2] == board[y][x+i+3]):
                return True

        # cols
        if (0 <= y+i and y+i < COLS):
            if (board[y+i][x] == board[y+i+1][x] == board[y+i+2][x] == board[y+i+3][x]):
                return True

        # /
        if (0 <= x+i and 0 <= y+i and x+i < ROWS and y+i < COLS):
            if (board[y+i][x+i] == board[y+i+1][x+i+1] == board[y+i+2][x+i+2] == board[y+i+3][x+i+3]):
                return True

        # \
        if (0 <= x+i and 0 <= y-i and x+i < ROWS and y-i < COLS):
            if (board[y-i][x+i] == board[y-i-1][x+i+1] == board[y-i-2][x+i+2] == board[y-i-3][x+i+3]):
                return True

    return False


while (True):
    print("\nPlayer", turn+1, "\n")
    printBoard()

    while (True):
        print("Move: ", end="")
        a = int(input())
        if (1 > a or a > COLS or lowest[a-1] == ROWS):
            print("Invalid input.\n")
        else:
            break

    board[lowest[a-1]][a-1] = ("X" if turn == 0 else "O")

    if (checkWinner(a-1, lowest[a-1])):
        print("\nPlayer", turn+1, "won!\n")
        printBoard()
        break

    lowest[a-1] += 1

    turn = (turn+1)%2