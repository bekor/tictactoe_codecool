# 
#
#  Tic-tac-toe is a game for two payers, X and O, who take turns marking the spaces
#  in a 3x3 grid. The payer who succeeds in placing three of their marks in a horizontal,
#  verical or diagonal row wins the game. More @ https://en.wikipedia.org/wiki/Tic-tac-toe
#
#
#  This program is running in terminal.
#
import sys
import string
from random import randint
from game_board import board_value, print_board
from win_condition import check_board_value
import get_input

poss_alpha_inputs = string.ascii_uppercase[:9]
poss_num_inputs = string.digits[1:]

BOARD = []



def player_move(sign):
    while True:
        player_coord = get_input.get_coordinate_input(poss_alpha_inputs, poss_num_inputs)
        value = BOARD[player_coord[0]][player_coord[1]]
        if value == " ":
            BOARD[player_coord[0]][player_coord[1]] = sign
            return player_coord
        else:
            print("Wrong coordinates \n%s player try other coords" % sign)        


def win_sequence_lenght(size):
    if size > 3 and size < 8:
        size = 4
    elif size > 8:
        size = 5
    print("Put {} same sign to win".format(size))
    return size


def ai_move(size, win_seq, alpha_inputs):
    while True:
        ai_row = randint(0, size - 1)
        ai_column = randint(0, size - 1)
        ai_value = BOARD[ai_row][ai_column]
        if ai_value == " ":
            BOARD[ai_row][ai_column] = "o"
            print_board(size, BOARD, alpha_inputs)
            win_cond = check_board_value(ai_row, ai_column, "o", BOARD, size, win_seq)
            return win_cond


def game():
    ai = get_input.play_mode()
    size = get_input.get_board_size()
    win_seq = win_sequence_lenght(size)
    board_value(size, BOARD)
    print_board(size, BOARD, poss_alpha_inputs)
    counter = 1
    win_cond = False
    while counter < (size**2 + 1):
        
        if counter % 2 != 0:
            player_coord = player_move("x")
            print_board(size, BOARD, poss_alpha_inputs)
            if check_board_value(player_coord[0], player_coord[1], "x", BOARD, size, win_seq):
                print("X Player Win!")
                break

        if not ai:          
            if counter % 2 == 0:
                player_coord = player_move("o")
                print_board(size, BOARD, poss_alpha_inputs)
                if check_board_value(player_coord[0], player_coord[1], "o", BOARD, size, win_seq):
                    print("O Player Win!")
                    break

        else:
            if counter % 2 == 0:
                ai_coord = ai_move(size, win_seq, poss_alpha_inputs)
                if ai_coord:
                    print("AI Win!")
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
