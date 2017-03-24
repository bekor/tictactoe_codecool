def check_board_value(row, column, sign, board, size, win_amount):
    res_row = res_column = res_diag1 = res_diag2 = False
    board_row_list = []
    board_column_list = []
  
    for i in range(size):
        board_row_list.append(board[row][i])
    res_row = check_win_condition(board_row_list, sign, win_amount)
    for i in range(size):
        board_column_list.append(board[i][column])
    res_column = check_win_condition(board_column_list, sign, win_amount)    
    
    res_diag1 = check_diagonals(board, size, sign, win_amount)
    res_diag2 = check_diagonals(board[::-1], size, sign, win_amount)

    return (res_column or res_row or res_diag1 or res_diag2)


def check_diagonals(board, size, sign, win_amount):
    board_diag = []
    for size_runner in range(size+1):
        for i in range(size_runner):
            second_coord = size_runner - i - 1
            board_diag.append(board[i][second_coord])
        win_check = check_win_condition(board_diag, sign, win_amount)
        if win_check:
            return True
        board_diag = []
        for i in range(size_runner):
            second_coord = size_runner - i - 1
            board_diag.append(board[i][-(second_coord + 1)])
        win_check = check_win_condition(board_diag, sign, win_amount)
        if win_check:
            return True
        board_diag = []
    return False


def check_win_condition(board_list, sign, win_amount):
    if (win_amount * sign) in "".join(board_list):
        return True
    else:
        return False