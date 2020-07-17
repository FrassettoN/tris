import random
from math import floor

human_pos = []
computer_pos = []


def board():
    board = human_pos + computer_pos
    return board


def computer():
    pos = random.randint(1, 9) - 1
    if pos not in board():
        computer_pos.append(pos)
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
    if pos not in board():
        human_pos.append(pos)
    else:
        giocatore()


def print_board():
    board_to_print = []
    for pos in range(9):
        board_to_print.append(" ")

    for pos in human_pos:
        board_to_print[pos] = 'X'

    for pos in computer_pos:
        board_to_print[pos] = 'O'

    for i in range(3):
        livello = []
        for j in range(i * 3, i * 3 + 3):
            livello.append(board_to_print[j])
        print(livello)


schemi_vittoria = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 5]
]


def controlla_vittoria(player):
    positions = human_pos if player == "giocatore" else computer_pos
    for schema in schemi_vittoria:
        vittory = True
        for n in schema:
            if n not in positions:
                vittory = False
        if vittory:
            break

    if vittory:
        return f'Ha vinto il {player}'
    if len(board()) == 9:
        return 'Parità'


result = None
while not result:
    giocatore()
    result = controlla_vittoria('giocatore')
    if not result:
        computer()
        result = controlla_vittoria('computer')
    if result:
        print(result)
    print_board()
