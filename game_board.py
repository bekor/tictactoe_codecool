import os


def value_board_value(size):
    for i in range(size):
        value_board.append([" "] * size)


def print_board(size):
    os.system('clear')
    print_first_row = []
    print_rows = []
    print("\n")
    for i in range(size):
        print_first_row.append(" " + poss_alpha_inputs[i]+"  ")
    print("   " + "".join(print_first_row))
    for i in range(size):
        for j in range(size):
            if j == 0:
                print_rows.append("  " + value_board[i][j])                                
            else:    
                print_rows.append(" | " + value_board[i][j])
        print(" %s" % (i + 1) + "".join(print_rows))
        print_rows = []
        print("   " + "-" * (size * 4 -1))
