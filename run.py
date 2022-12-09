import random


def design_board(marks):
    """
    generates a 3 x 3 board of 9 spaces using a dictionary
    that corresponds to the numbers on a keypad / telephone
    """
    board = (f"{marks[1]}|{marks[2]}|{marks[3]}\n"
            f"{marks[4]}|{marks[5]}|{marks[6]}\n"
            f"{marks[7]}|{marks[8]}|{marks[9]}")
    print(board)


def choose_mark():
    """
    asks user to pick a 'x' or 'o' as their mark
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
        # validates user's input against available board spaces
        if user_input not in available_spaces:
            print("Please choose a free space")
            continue
        # removes user's choice from available numbers
        available_spaces.remove(user_input)
        # replaces the placeholder number on board with user's mark (x or o)
        marks[user_input] = user_selection
        break


def check_winner(marks):
    """
    check whether there is 3 in a row of either mark (x / o)
    """
    # Check horizontal 3 in a row
    if (marks[1] == marks[2] == marks[3]) \
        or (marks[4] == marks[5] == marks[6]) \
        or (marks[7] == marks[8] == marks[9]):
        print(f"{current_player} wins!")
        return True
    # Check vertical 3 in a row
    elif (marks[1] == marks[4] == marks[7]) \
        or (marks[2] == marks[5] == marks[8]) \
        or (marks[3] == marks[6] == marks[9]):
        print(f"{current_player} wins!")
        return True
    # Check diagonal 3 in a row
    elif (marks[1] == marks[5] == marks[9]) \
        or (marks[3] == marks[5] == marks[7]):
        print(f"{current_player} wins!")
        return True


def computer_turn():
    """
    selects a random number for the computer from available
    list of numbers"""
    print("Computer's turn: ")
    # shuffles list of available numbers
    random.shuffle(available_spaces)
    # chooses random number from list of available numbers
    computer_input = random.choice(available_spaces)
    # removes computer's choice from available numbers
    available_spaces.remove(computer_input)
    # replaces the placeholder number on board with computer's mark (x or o)
    marks[computer_input] = computer_selection


marks = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
available_spaces = [1,2,3,4,5,6,7,8,9]
declare_winner = False
turn = 0
current_player = None

user_selection = choose_mark()
computer_selection = computer_mark(user_selection)
design_board(marks)

while not declare_winner:
    # declares a draw if board is full and there's no winner
    if turn == 9:
        print("It's a stalemate!")
        break

    # iterates turn if there are available spaces on the board
    while available_spaces:
        if turn % 2 == 0:
            user_turn()
            current_player = "User"
        else:
            computer_turn()
            current_player = "Computer"
        design_board(marks)
        declare_winner = check_winner(marks)
        turn += 1
        break
