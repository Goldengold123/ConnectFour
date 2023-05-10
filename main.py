import pygame as pg

TICK_SPEED = 60
ROWS = 6
COLS = 7

WIDTH = 60 + COLS * 55
HEIGHT = 120 + ROWS * 55

COLOUR_WHITE = (255, 255, 255)
COLOUR_BLACK = (0, 0, 0)
COLOUR_BLUE = (0, 0, 255)
COLOUR_YELLOW = (255, 255, 0)
COLOUR_RED = (255, 0, 0)
COLOUR_GREY = (128, 128, 128)

board = [[" " for i in range(COLS)] for j in range(ROWS)]
lowest = [0 for i in range(COLS)]
turn = 0

mouseX = -1
mouseXidx = -1


def printBoard():
    for i in range(ROWS):
        for j in range(COLS):
            print(board[5-i][j], end="|")
        print()
    print()


def mouseIdx(m):
    if m <= 35 or m >= WIDTH - 35:
        return -1
    if 30 <= m % 55 <= 35:
        return -1
    return (m - 35) // 55


def drawTitle(s):
    font = pg.font.Font('freesansbold.ttf', 32)
    title = font.render("Connect Four", True, COLOUR_BLACK)
    titleRect = title.get_rect()
    titleRect.center = (WIDTH // 2, 20)
    s.blit(title, titleRect)
    font2 = pg.font.Font('freesansbold.ttf', 18)
    pTurn = font2.render(("Player " + str(turn + 1) + " to move."), True, COLOUR_BLACK)
    pTurnRect = pTurn.get_rect()
    pTurnRect.center = (WIDTH // 2, 60)
    s.blit(pTurn, pTurnRect)


def drawBoard(s):
    pg.draw.rect(s, COLOUR_BLUE, pg.Rect(30, 90, 55 * COLS + 5, 55 * ROWS + 5))
    for i in range(COLS):
        for j in range(ROWS):
            x = 60 + 55 * i
            y = 120 + 55 * j
            if j == lowest[i] and i == mouseXidx:
                colour = COLOUR_GREY
            elif board[j][i] == " ":
                colour = COLOUR_WHITE
            elif board[j][i] == "X":
                colour = COLOUR_YELLOW
            else:
                colour = COLOUR_RED
            pg.draw.circle(s, colour, (x, 65 + HEIGHT - y), 25)


def checkWinner(x, y):
    for i in range(-3, 1):
        # rows
        if 0 <= x + i < ROWS-3:
            if board[y][x + i] == board[y][x + i + 1] == board[y][x + i + 2] == board[y][x + i + 3]:
                return True

        # cols
        if 0 <= y + i < COLS-3:
            if board[y + i][x] == board[y + i + 1][x] == board[y + i + 2][x] == board[y + i + 3][x]:
                return True

        # /
        if 0 <= x + i < ROWS-3 and 0 <= y + i < COLS-3:
            if board[y + i][x + i] == board[y + i + 1][x + i + 1] == board[y + i + 2][x + i + 2] == board[y + i + 3][x + i + 3]:
                return True

        # \
        if 0 <= x + i < ROWS-3 and 3 <= y - i < COLS:
            if board[y - i][x + i] == board[y - i - 1][x + i + 1] == board[y - i - 2][x + i + 2] == board[y - i - 3][x + i + 3]:
                return True

    return False


# init pygame
pg.init()
pg.display.set_caption("Connect Four!")
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(COLOUR_WHITE)
clock = pg.time.Clock()


turn = 0
done = False

while not done:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONUP:
            # mouse position
            mouseX = pg.mouse.get_pos()[0]
            mouseXidx = mouseIdx(mouseX)

            if 0 <= mouseXidx < COLS and lowest[mouseXidx] < ROWS:
                board[lowest[mouseXidx]][mouseXidx] = ("X" if turn == 0 else "O")
            if checkWinner(mouseXidx, lowest[mouseXidx]):
                print("\nPlayer", turn + 1, "won!\n")
                drawBoard(screen)
                done = True
                break

            lowest[mouseXidx] += 1

            turn = (turn + 1) % 2

        if event.type == pg.QUIT:
            done = True
    # mouse position
    mouseX = pg.mouse.get_pos()[0]
    mouseXidx = mouseIdx(mouseX)

    # display
    screen.fill(COLOUR_WHITE)
    drawTitle(screen)
    drawBoard(screen)
    pg.display.flip()
    clock.tick(TICK_SPEED)