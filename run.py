import random
import os
import sys
import time


def design_board(available_spaces):
    """
    generates a 3 x 3 board of 9 spaces using a dictionary
    that corresponds to the numbers on a keypad / telephone
    """
    os.system("cls||clear")
    simulate_typing(spaces[1]+'|'+spaces[2]+'|'+spaces[3])
    simulate_typing(spaces[4]+'|'+spaces[5]+'|'+spaces[6])
    simulate_typing(spaces[7]+'|'+spaces[8]+'|'+spaces[9])


def choose_mark():
    """
    asks user to pick a 'x' or 'o' as their mark
    """
    user_choice = None
    while user_choice not in {"x", "o"}:
        user_choice = input('Please select "o" or "x"\n')
    return user_choice


def computer_mark(string):
    """
    determines computer's mark based on user's input
    """
    computer_choice = "x" if user_selection == "o" else "o"
    return computer_choice


def first_turn():
    """
    randomises the first turn to make the game more difficult
    """
    random_turn = random.choice([1, 0])
    return random_turn


def user_turn():
    """
    asks user to choose a space, removes choice from available list,
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
        spaces[user_input] = user_selection
        break


def check_winner(dictionary):
    """
    check whether there is 3 in a row of either mark (x / o)
    """

    if (
        (spaces[1] == spaces[2] == spaces[3])
        or (spaces[4] == spaces[5] == spaces[6])
        or (spaces[7] == spaces[8] == spaces[9])
    ):
        simulate_typing(f"{current_player} wins!")
        return True
    # check vertical 3 in a row
    elif (
        (spaces[1] == spaces[4] == spaces[7])
        or (spaces[2] == spaces[5] == spaces[8])
        or (spaces[3] == spaces[6] == spaces[9])
    ):
        simulate_typing(f"{current_player} wins!")
        return True
    # check diagonal 3 in a row
    elif (
        (spaces[1] == spaces[5] == spaces[9])
        or (spaces[3] == spaces[5] == spaces[7])
    ):
        simulate_typing(f"{current_player} wins!")
        return True
    else:
        return False


def computer_turn():
    """
    selects a random number for the computer from available
    list of numbers"""
    simulate_typing("Computer's turn:    ")
    # shuffles list of available numbers
    random.shuffle(available_spaces)
    # chooses random number from list of available numbers
    computer_input = random.choice(available_spaces)
    # removes computer's choice from available numbers
    available_spaces.remove(computer_input)
    # replaces the placeholder number on board with computer's mark (x or o)
    spaces[computer_input] = computer_selection


def simulate_typing(string):
    """
    prints to the terminal as if typing
    """
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write("\n")


spaces = {
        1: "1", 2: "2", 3: "3", 4: "4", 5: "5",
        6: "6", 7: "7", 8: "8", 9: "9"
}
available_spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
declare_winner = False
current_player = None

os.system("cls||clear")
simulate_typing("Let's play NOUGHTS & CROSSES!")
user_selection = choose_mark()
computer_selection = computer_mark(user_selection)
design_board(spaces)

turn = first_turn()
current_player = "User" if turn == 0 else "Computer"
simulate_typing(f"{current_player} goes first     ")

while not declare_winner:
    # declares a draw if board is full and there's no winner
    if not available_spaces:
        simulate_typing("It's a stalemate!")
        break

    # iterates turn if there are available spaces on the board
    # alternates between user and computer
    while available_spaces:
        if turn % 2 == 0:
            user_turn()
            current_player = "User"
        else:
            computer_turn()
            current_player = "Computer"
        design_board(spaces)
        declare_winner = check_winner(spaces)
        turn += 1
        break
