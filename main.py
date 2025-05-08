import numpy as np

ary = np.array([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])
max_plays = 9
turn = 0


def check_victory() -> bool:
    for i in range(3):
        if ary[i][0] == ary[i][1] == ary[i][2] and ary[i][0] != " ":
            return True

        if ary[0][i] == ary[1][i] == ary[2][i] and ary[0][i] != " ":
            return True

    if ary[0][0] == ary[1][1] == ary[2][2] and ary[0][0] != " ":
        return True
    elif ary[0][2] == ary[1][1] == ary[2][0] and ary[0][2] != " ":
        return True

    return False


def print_board():
    print()
    for i in range(3):
        print(f" {ary[i][0]} | {ary[i][1]} | {ary[i][2]} ")
        if i < 2:
            print("---+---+---")
    print()


while turn != max_plays:
    print_board()

    play = [
        int(item) for item in input("Which position will you play [row][col] ej. 13: ")
    ]
    if turn % 2 == 0:
        sign = "X"
    else:
        sign = "O"

    try:
        if ary[play[0] - 1][play[1] - 1] == " ":
            ary[play[0] - 1][play[1] - 1] = sign
            turn += 1
            if check_victory():
                break

        else:
            print("Section filled choose another!")
    except IndexError:
        print("Input Not valid add values form 1-3")
    except ValueError:
        if play == "Exit":
            break
        else:
            print("Input Not valid add values form 1-3")

if turn != max_plays:
    if turn % 2 == 0:
        print("The O's have WON!!")
    else:
        print("The X's have WON!!")


else:
    if check_victory():
        print("The X's have WON!!")
    else:
        print("We have a DRAW :(")

print_board()
