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