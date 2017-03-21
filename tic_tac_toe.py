# 
#
#  Tic-tac-toe is a game for two payers, X and O, who take turns marking the spaces
#  in a 3x3 grid. The payer who succeeds in placing three of their marks in a horizontal,
#  verical or diagonal row wins the game. More @ https://en.wikipedia.org/wiki/Tic-tac-toe
#
#
#  This program is running in terminal.
#

from random import randint

list_of_possible_inputs = ("1", "2", "3")

# Set an empty 3x3 array
value_board = []
for i in range(3):
    value_board.append([" "] * 3)

def get_row_input():
    while True:
        r = input("row: ")
        if r in list_of_possible_inputs:
            return (int(r) - 1)
        else:
            print("Wrong row input")

def get_column_input():
    while True:
        c = input("column: ")
        if c in list_of_possible_inputs:
            return (int(c) -1)
        else:
            print("Wrong column input")

def print_board():
    print("\n")
    print(" " + " 1 " + " " + " 2 " + " " + " 3")
    for i in range(3):
        print("%s " %(i + 1) + value_board[i][0] +  " | " + value_board[i][1] + " | " + value_board[i][2])
        if i != 2:
            print(" -" * 6)

def check_win_contition(row, column, value):
    res_row = res_column = res_diag1 = res_diag2 = True

    for i in range(3):
        if value_board[row][i] != value:
            res_row = False
    for i in range(3):
        if value_board[i][column] != value:
            res_column = False
    for i in range(3):
        if value_board[i][i] != value:
            res_diag1 = False
    for i in range(3):
        if value_board[i][-(i+1)] != value:
            res_diag2 = False
    
    return (res_row or res_column or res_diag1 or res_diag2)

def play_mode():
    mode = input("Single Player: 1, Player vs Player: 2 : ")
    while True:
        if mode == "1":
            return True
        elif mode == "2":
            return False
        else:
            print("You did not choose mode!")

def player_move(win_cond, sign):
    a = True
    while a == True:
        player_row = get_row_input()
        player_column = get_column_input()
        value = value_board[player_row][player_column]
        if value == " ":
            value_board[player_row][player_column] = sign
            print_board()
            win_cond = check_win_contition(player_row, player_column, sign)
            if win_cond == True:
                print("%s Player Win!" % sign)
                return 1
            else:
                a = False
        else:
            print("Wrong coordonates \n%s player try other coords" % sign)

def game():
    ai = play_mode()
    print_board()
    counter = 1
    win_cond = False
    while counter < 10:
        
        if counter %2 != 0:
            x_player = player_move(win_cond, "x")
            if x_player == 1:
                break

        if not ai:          
            if counter %2 == 0:
                o_player = player_move(win_cond, "o")
                if o_player == 1:
                    break

        else:
            if counter %2 == 0:
                ai_row = randint(0, 2)
                ai_column = randint(0, 2)
                ai_value = value_board[ai_row][ai_column]
                if ai_value == " ":
                    value_board[ai_row][ai_column] = "o"
                    print_board()
                    win_cond = check_win_contition(ai_row, ai_column, "o")
                    if win_cond == True:
                        print("AI Win!")
                        break
                else:
                    counter -= 1
        counter += 1

game()
