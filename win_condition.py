def check_board_value(row, column, sign, board, size, win_amount):
    result = True
    board_row_list = []
    board_column_list = []
    board_diag1_list = []
    board_diag2_list = []
    
    for i in range(size):
        board_row_list.append(board[row][i])
        board_column_list.append(board[i][column])   
        board_diag1_list.append(board[i][i])
        board_diag2_list.append(board[i][-(i + 1)])

    check_win_condition(board_row_list, sign, win_amount)
    check_win_condition(board_column_list, sign, win_amount)
    check_win_condition(board_diag1_list, sign, win_amount)
    check_win_condition(board_diag2_list, sign, win_amount)

    return result


def check_win_condition(board_list, sign, win_amount):
    if (win_amount * sign) in board_list:
        result = False