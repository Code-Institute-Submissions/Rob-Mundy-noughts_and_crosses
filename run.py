import random


def design_board(marks):
    """
    creates initial board of 9 spaces using a dictionary
    that corresponds to the numbers on a keypad/telephone
    """
    board = (f"{marks[1]}|{marks[2]}|{marks[3]}\n"
            f"{marks[4]}|{marks[5]}|{marks[6]}\n"
            f"{marks[7]}|{marks[8]}|{marks[9]}")
    print(board)


def choose_mark():
    """
    asks user to pick an 'x' or 'o'
    """
    user_choice = None
    while user_choice not in {'x', 'o'}:
        user_choice = input('Please select "x" or "o"\n')
    return user_choice


def computer_mark(user_selection):
    """
    determines computer's mark based on user's input
    """
    computer_choice = 'x' if user_selection == 'o' else 'o'
    return computer_choice


def user_turn():
    """
    Asks user to choose a space, removes choice from available list,
    places user's mark on the board
    """
    while True:
        try:
            user_input = int(input("Your turn: "))
        except ValueError:
            print("That isn't available. Try again: ")
            continue
        if user_input not in available_spaces:
            print("Please choose a free space")
            continue
        available_spaces.remove(user_input)
        marks[user_input] = user_selection
        # design_board(marks)
        break


def check_winner(marks):
    """
    check whether there is 3 in a row of either mark (x/o)
    """
    # Check horizontal 3 in a row
    if (marks[1] == marks[2] == marks[3]) \
        or (marks[4] == marks[5] == marks[6]) \
        or (marks[7] == marks[8] == marks[9]):
        print("We have a winner!")
        return True
    # Check vertical 3 in a row
    elif (marks[1] == marks[4] == marks[7]) \
        or (marks[2] == marks[5] == marks[8]) \
        or (marks[3] == marks[6] == marks[9]):
        print("We have a winner!")
        return True
    # Check diagonal 3 in a row
    elif (marks[1] == marks[5] == marks[9]) \
        or (marks[3] == marks[5] == marks[7]):
        print("We have a winner!")
        return True



def computer_turn():
    """
    selects a random number for the computer from available
    list of numbers"""
    print("Computer's turn: ")
    random.shuffle(available_spaces)
    computer_input = random.choice(available_spaces)
    available_spaces.remove(computer_input)
    marks[computer_input] = computer_selection
    # design_board(marks)


marks = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
available_spaces = [1,2,3,4,5,6,7,8,9]
declare_winner = False
turn = 0

user_selection = choose_mark()
computer_selection = computer_mark(user_selection)
design_board(marks)

while not declare_winner:

    while available_spaces:

        if turn % 2 == 0:
            user_turn()
        else:
            computer_turn()
        turn += 1
        design_board(marks)
        declare_winner = check_winner(marks)
        break
