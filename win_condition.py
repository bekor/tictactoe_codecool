def check_board_value(row, column, sign, board, size, win_amount):
    res_row = res_column = res_diag1 = res_diag2 = False
    board_row_list = []
    board_column_list = []
    board_diag1_list = []
    board_diag2_list = []

    #print(board)
    
    for i in range(size):
        board_row_list.append(board[row][i])
    res_row = check_win_condition(board_row_list, sign, win_amount)
    for i in range(size):
        board_column_list.append(board[i][column])
    res_row = check_win_condition(board_row_list, sign, win_amount)    
    for i in range(size):
        board_diag1_list.append(board[i][i])
    res_diag1 = check_win_condition(board_diag1_list, sign, win_amount)
    for i in range(size):   
        board_diag2_list.append(board[i][-(i + 1)])
    res_diag2 = check_win_condition(board_diag2_list, sign, win_amount)
    if size >= 5:
        

    
    
    print(board_row_list)
    print(board_column_list)
    #print(board_diag1_list)
    #print(board_diag2_list)
    #print(res_column or res_row or res_diag1 or res_diag2)
    return (res_column or res_row or res_diag1 or res_diag2)


def check_win_condition(board_list, sign, win_amount):
    if (win_amount * sign) in "".join(board_list):
        return True
    else:
        return False