import random


def design_board(marks):
    """
    creates initial board of 9 spaces using a dictionary/n
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
    # print(f"You chose {user_choice}")
    return user_choice


def computer_mark(user_selection):
    """
    determines computer's choice based on user's input
    """
    computer_choice = 'x' if user_selection == 'o' else 'o'
    # print(f"Computer is {computer_choice}")
    return computer_choice


def user_turn():
    """
    Asks user to choose a space,
    removes choice from available list,
    places user's mark on the board
    """
    while True:
        try:
            user_input = int(input("Choose your space: "))
        except ValueError:
            print("Please choose a free space")
            continue
        if user_input in available_spaces:
            print(f'You chose {user_input}')
            available_spaces.remove(user_input)
            print(available_spaces)
            # update_marks(marks)
        break


def which_turn():
    """
    determines whether it is the user's turn or
    the computer's
    """
    turn = 0
    if turn % 2 == 0:
        user_turn()
    else:
        computer_turn()
    turn += 1
    # print(f'Turn is {turn}')

# def update_available()
    # check free spaces
    # could use separate list?

# def check_winner()
    # check whether there is 3 in a row of either mark (x/o)

# def check_full()
    # are there any spaces left to place a mark?
    # could the which_turn function incorporate this?


def computer_turn():
    """
    selects a random number for the computer
    from available list of numbers"""
    computer_input = random.choice(available_spaces)
    print(f'Computer chose {computer_input}')
    available_spaces.remove(computer_input)
    print(available_spaces)


def main():
    """
    Run all game functions
    """
    user_selection = choose_mark()
    computer_selection = computer_mark(user_selection)
    # print(f"Place your mark on the board\nby entering a number between\n1 and 9")
    design_board(marks)
    which_turn()



marks = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
available_spaces = [1,2,3,4,5,6,7,8,9]
print("let's begin!")
main()
