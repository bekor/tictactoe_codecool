import os


def board_value(size, value_b):
    for i in range(size):
        value_b.append([" "] * size)


def print_board(size, value_b, p_alpha):
    os.system('clear')
    print_first_row = []
    print_rows = []
    print("\n")
    for i in range(size):
        print_first_row.append(" " + p_alpha[i]+"  ")
    print("   " + "".join(print_first_row))
    for i in range(size):
        for j in range(size):
            if j == 0:
                print_rows.append("  " + value_b[i][j])
            else:
                print_rows.append(" | " + value_b[i][j])
        print(" %s" % (i + 1) + "".join(print_rows))
        print_rows = []
        if i <= (size-2):
            print("   " + "-" * (size * 4 - 1))


