# 
#
#  Tic-tac-toe is a game for two payers, X and O, who take turns marking the spaces
#  in a 3x3 grid. The payer who succeeds in placing three of their marks in a horizontal,
#  verical or diagonal row wins the game. More @ https://en.wikipedia.org/wiki/Tic-tac-toe
#
#
#  This program is running in terminal.
#
import string
from random import randint
from game_board import board_value, print_board
import get_input

poss_alpha_inputs = string.ascii_uppercase[:9]
poss_num_inputs = string.digits[1:]

BOARD = []


def check_win_contition(row, column, value):
    res_row = res_column = res_diag1 = res_diag2 = True

    for i in range(3):
        if BOARD[row][i] != value:
            res_row = False
    for i in range(3):
        if BOARD[i][column] != value:
            res_column = False
    for i in range(3):
        if BOARD[i][i] != value:
            res_diag1 = False
    for i in range(3):
        if BOARD[i][-(i+1)] != value:
            res_diag2 = False
    
    return (res_row or res_column or res_diag1 or res_diag2)


def player_move(sign):
    while True:
        player_coord = get_input.get_coordinate_input(poss_alpha_inputs, poss_num_inputs)
        value = BOARD[player_coord[0]][player_coord[1]]
        print(player_coord)
        if value == " ":
            BOARD[player_coord[0]][player_coord[1]] = sign
            return player_coord
        else:
            print("Wrong coordinates \n%s player try other coords" % sign)        


def game():
    ai = get_input.play_mode()
    size = get_input.get_board_size()
    board_value(size, BOARD)
    print_board(size, BOARD, poss_alpha_inputs)
    counter = 1
    win_cond = False
    while counter < 10:
        
        if counter % 2 != 0:
            player_coord = player_move("x")
            print_board(size, BOARD, poss_alpha_inputs)
            if check_win_contition(player_coord[0], player_coord[1], "x"):
                print("X Player Win!")
                break

        if not ai:          
            if counter % 2 == 0:
                player_coord = player_move("o")
                print_board(size, BOARD, poss_alpha_inputs)
                if check_win_contition(player_coord[0], player_coord[1], "o"):
                    print("O Player Win!")
                    break

        else:
            if counter % 2 == 0:
                ai_row = randint(0, 2)
                ai_column = randint(0, 2)
                ai_value = BOARD[ai_row][ai_column]
                if ai_value == " ":
                    BOARD[ai_row][ai_column] = "o"
                    print_board(size, BOARD, poss_alpha_inputs)
                    win_cond = check_win_contition(ai_row, ai_column, "o")
                    if win_cond == True:
                        print("AI Win!")
                        break
                else:
                    counter -= 1
        counter += 1
         

def main():
    while True:
        global BOARD
        game()
        get_input.replay_or_exit()
        BOARD = []


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print("You terminated the beauty of the Tic-Tac-Toe")
        print('You pressed Ctrl+C!')
        sys.exit()
