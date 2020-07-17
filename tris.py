import random
from math import floor


def create_board():
    board = []
    for i in range(3):
        livello = []
        for j in range(3):
            livello.append(" ")
        board.append(livello)
    return board


board = create_board()


def computer():
    pos = random.randint(1, 9) - 1
    row = floor(pos / 3)
    col = pos % 3
    if board[row][col] == " ":
        board[row][col] = 'X'
    else:
        computer()


def get_int(ask, min, max):
    try:
        result = int(input(ask))
        if int(result) < min or int(result) > max:
            return get_int(ask, min, max)
        else:
            return int(result)
    except ValueError:
        return get_int(ask, min, max)


def giocatore():
    pos = get_int("Posizione: ", 1, 10) - 1
    row = floor(pos / 3)
    col = pos % 3
    if pos < 9 and board[row][col] == " ":
        board[row][col] = 'O'
    else:
        giocatore()


def print_board(board):
    for livello in board:
        print(livello)


schemi_vittoria = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 6]
]


def controlla_vittoria(board, sign_to_check):
    for sign in [sign_to_check, " "]:
        positions = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == sign:
                    positions.append(i * 3 + j + 1)
        if sign == " " and len(positions) == 0:
            return 'parità'

        for schema in schemi_vittoria:
            vittory = True
            for n in schema:
                if n not in positions:
                    vittory = False
            if vittory:
                break

        if vittory and sign != " ":
            return sign


result = None
while not result:
    giocatore()
    result = controlla_vittoria(board, 'O')
    if not result:
        computer()
        result = controlla_vittoria(board, 'X')
    if result:
        print(f"Ha vinto {result}")
    print_board(board)
