#Tic tac toe

"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Martin Gabriel
email: gabmar@post.com
"""

import random
import time

def print_vertical_separator():
    print("========================================")


def generate_board(GRID_SIZE : int):

    board = [[" " for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    return board


def print_board(board, GRID_SIZE : int):

    string = ""

    for i in range(GRID_SIZE):
        line = "   " + GRID_SIZE * "+---" + "+\n" + str(i + 1) + f"{" " if len(str(i + 1)) == 2 else "  "}"
        for j in range(GRID_SIZE):
            line = line + f"| {board[j][i]} "
        string = string + line + "|\n"

    string = string + "   " + GRID_SIZE * "+---" + "+\n"

    line = "     "
    for k in range(GRID_SIZE):
        line = line + chr(97 + k) + "   "
    string = string + line + "\n"

    print(string)


def player_turn(board, player : str, GRID_SIZE: int):

    error_message = "Invalid coordinate. Please try again."
    
    while True:
        move = input(f"Player {player}, enter your move.\n").strip()
        column = move[0]
        row = move[1:]

        #move verification
        if ord(column) - 96 - 1 not in range(GRID_SIZE):
            print(error_message)
            continue

        elif not row.isdecimal() or int(row) - 1 not in range(GRID_SIZE):
            print(error_message)
            continue

        elif board[ord(column) - 96 - 1][int(row) - 1] != " ":
            print(error_message)
            continue

        else:
            break

    #move is valid
    board[ord(column) - 96 - 1][int(row) - 1] = player

    return (column, row)


def end_check(board, GRID_SIZE: int):

    #columns check
    for i in range(GRID_SIZE):
        player = board[i][0]
        if player == " ":
            continue
        for j in range(GRID_SIZE):
            if board[i][j] != player:
                break
        else:
            return player
        
    #rows check
    for i in range(GRID_SIZE):
        player = board[0][i]
        if player == " ":
            continue
        for j in range(GRID_SIZE):
            if board[j][i] != player:
                break
        else:
            return player
        
    #diagonals check
    player = board[0][0]
    for i in range(GRID_SIZE):
        if board[i][i] == " " or player != board[i][i]:
            break
    else:
        return player
    
    player = board[0][GRID_SIZE - 1]
    for i in range(GRID_SIZE):
        if board[i][(GRID_SIZE - 1) - i] == " " or player != board[i][(GRID_SIZE - 1) - i]:
            break
    else:
        return player
    
    #draw check
    for column in board:
        for position in column:
            if position == " ":
                return False
    return "draw"


def coin_flip(player):
    time.sleep(random.uniform(2, 4))
    print(f"  _____  \n /     \ \n|   {player}   |\n \_____/\n")
    time.sleep(1)


def tic_tac_toe(GRID_SIZE=3):

    #introduction
    print("Welcome to Tic Tac Toe!")
    print_vertical_separator()
    print("GAME RULES:")
    print(f"Each player can place one mark (or stone) per turn on the {GRID_SIZE}x{GRID_SIZE} grid.\n")
    print(f"The WINNER is who succeeds in placing {GRID_SIZE} of their marks in a:")
    print("* horizontal,\n* vertical or\n* diagonal row")
    print_vertical_separator()

    #random player selection
    print("Let's flip a coin to see which player will start.")
    player = "O" if random.randint(0,1) else "X"
    #stupid coin flip visual (optional)
    coin_flip(player)
    print(f"Player {player} begins. Let's start the game.\n")

    #playing board generation
    board = generate_board(GRID_SIZE)
    print_board(board, GRID_SIZE)
    end = False
    
    while not end:
        player_turn(board, player, GRID_SIZE)
        end = end_check(board, GRID_SIZE)
        print_board(board, GRID_SIZE)
        player = "O" if player == "X" else "X"

    if end == "X" or end == "O":
        print(f"Congratulations player {end}, you have won!")
    if end == "draw":
        print("It's a draw! Neither player wins.")


tic_tac_toe(3)
