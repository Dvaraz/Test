# 1 Draw a field
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']


def check_for_winner():
    global winner
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    collumn_1 = board[0] == board[3] == board[6] != "-"
    collumn_2 = board[1] == board[4] == board[7] != "-"
    collumn_3 = board[2] == board[5] == board[8] != "-"
    diagonal_1 = board[2] == board[4] == board[6] != "-"
    diagonal_2 = board[0] == board[4] == board[8] != "-"
    if row_1 or row_2 or row_3:
        print(f"Win {player_turn1}")
        winner = 1
    elif collumn_1 or collumn_2 or collumn_3:
        print(f"Win {player_turn1}")
        winner = 1
    elif diagonal_1 or diagonal_2:
        print(f"Win {player_turn1}")
        winner = 1
    elif "-" not in board:
        print("Draw")
        quit()

def draw_board():

    """
    Drawing board according to board list.
    :return: 
    """
    print(board[0] + "|" + board[1] + '|' + board[2])
    print(board[3] + "|" + board[4] + '|' + board[5])
    print(board[6] + "|" + board[7] + '|' + board[8])



winner = 0
game_on = True
turn = 1  # turn = 1 is player_1 chose, turn = 0 is player_2 chose.
player_turn1 = "Player_1"
taken_position2 = []
taken_positions = {}


def player_turn(player):
    turn = True
    global player_turn1
    if player == "Player_1":
        player_turn1 = "Player_2"
    elif player == "Player_2":
        player_turn1 = "Player_1"
    player_def = ""
    if player == "Player_1":
        player_def = "X"
    elif player == "Player_2":
        player_def = "O"

    while turn:  # gives turn to player_1, checking that player took empty cell.
        check_for_winner()
        if winner == 1:
            quit()
        player_chose = input(f"It is {player}, please chose a cell in range from 0 to 8: ")
        try:
            player_chose = int(player_chose)
            if player_chose in taken_positions or player_chose > len(board) - 1:
                print("You can not go here chose different position: ")
            else:
                taken_positions[player_chose] = taken_positions.get(player_chose, 1)
                board[player_chose] = player_def
                turn = False
        except ValueError:
            print("Wrong Input.Try one more time.")


def game_start():
    global game_on
    global turn
    global winner
    while game_on is True:
        draw_board()
        player_turn(player_turn1)


game_start()
