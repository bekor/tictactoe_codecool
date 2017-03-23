def play_mode():
    while True:
        mode = input("Single Player: 1, Player vs Player: 2 : ")
        if mode == "1":
            return True
        elif mode == "2":
            return False
        else:
            print("You did not choose mode!")


def get_board_size():
    while True:
        try:
            size_input = int(input("Choose board size(3-9): "))
            if size_input >= 3 and size_input <= 9:
                return size_input
            else:
                print("Please choose valid size!")
        except ValueError:
            print("Please enter a number(3-9)!")


def get_coordinate_input(p_alpha, p_num):
    while True:
        raw_coordinate = input("Insert coordinates (like: A1): ")
        if (raw_coordinate[0].upper() in p_alpha) and \
           (raw_coordinate[1] in p_num):
            coord = []
            coord.append(int(raw_coordinate[1])-1)
            coord.append(p_alpha.index(raw_coordinate[0]))
            return coord
        else:
            print("Wrong row input")


def replay_or_exit():
    while True:
        replay_or_exit = input("Do you want to play again(Y) or quit(Q): ")
        if replay_or_exit.upper() == "Y":
            return True
        elif replay_or_exit.upper() == "Q":
            exit()
        else:
            print("You have not decided!")