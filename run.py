marks = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}

def design_board(marks):
    """
    creates initial board of 9 spaces using a dictionary/n
    that corresponds to the numbers on a keypad/telephone
    """
    board = (f"{marks[1]}|{marks[2]}|{marks[3]}|{marks[4]}|{marks[5]}|{marks[6]}|{marks[7]}|{marks[8]}|{marks[9]}")
    print(board)


design_board(marks)

#def choose_mark()
    #asks user to pick an 'x' or 'o'
    #computer defaults to !user

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



