#dictionary of marks i.e. spaces where x's and o's can be marked
#numbered key as key will be visible and values are letters
marks = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}

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
    #computer defaults to !user
    user_choice = None
    while user_choice not in {'x', 'o'}:
        user_choice = input('Please select "x" or "o"\n')
    print(f"You chose {user_choice}")
    return user_choice
    
    

def computer_mark(user_selection):
    """
    determines computer's choice based on
    user's input
    """
    computer_choice = 'x' if user_selection == 'o' else 'o'
    print(f"Computer is {computer_choice}")
    return computer_choice
    
    


#def which_turn()
    #determines whether it is the user or computer's turn
    #use modulo?
    #improve: randomise first attempt to see who goes first

#def check_board()
    #check free spaces
    #could use separate list?

#def check_winner()
    #check whether there is 3 in a row of either mark (x/o)

#def check_full()
    #are there any spaces left to place a mark?
    #could the which_turn function incorporate this?

#def computer_turn()
    #random computer guess
    # improve: apply some logic to make it more difficult?

def main():
    """
    Run all game functions
    """
    design_board(marks)
    user_selection = choose_mark()
    computer_selection = computer_mark(user_selection)
    print(f"Place your mark on the board\nby entering a number between\n1 and 9")

print("let's begin!")
main()
