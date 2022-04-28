"""
Tic-tac-toe game by Melody Curran
"""

def main():
    print()

    # Creates list of numbers to be displayed on tic-tac-toe board
    get_list = create_tic_tac_toe_list()

    # Prints empty board
    create_board(get_list)

    print()

    # While loop so players could take turns
    while is_winner(get_list) == False:
     
        print()
        # Player X's turn
        x = int(input('It\'s X\'s turn to choose square (Type 1-9): '))
        print()
        # Calling take turn function to replace the chosen number with X
        take_x_turn(x, get_list)
        # If player X has not won yet, the player O will take turn
        if not is_winner(get_list):
            print()
            # Player O's turn
            o = int(input('It\'s O\'s turn to choose square (Type 1-9): '))
            print()
            take_o_turn(o, get_list)
    else:
        print('Thanks for playing!')
         
def create_tic_tac_toe_list():
    """
    This function creates a list of number from 1-9
    to display to tic-tac-toe board
    """
    rows = []
    for i in range(1, 10):
        rows.append(i) 
    return rows


def create_board(get_list):
    """
    This function prints out the board with numbers
    """
    print(f'{get_list[0]} | {get_list[1]} | {get_list[2]}')
    print('--+---+---')
    print(f'{get_list[3]} | {get_list[4]} | {get_list[5]}')
    print('--+---+---')
    print(f'{get_list[6]} | {get_list[7]} | {get_list[8]}') 


def take_x_turn(x, get_list):
    """
    This function replaces the chosen number with X
    """
    i = get_list.index(x)
    get_list[i] = 'X'

    return create_board(get_list)
    

def take_o_turn(o, get_list):
    """
    This function replaces the chosen number with O
    """
    i = get_list.index(o)
    get_list[i] = 'O'

    return create_board(get_list)

def is_winner(get_list):
    """
    This function is to determine if one the players has won
    """
    msg = 'Congrats you won!'

    if (get_list[0] == 'X' and get_list[1] == 'X' and get_list[2] == 'X') or (get_list[0] == 'O' and get_list[1] == 'O' and get_list[2] == 'O'):
        print(msg)
        return True
    elif (get_list[3] == 'X' and get_list[4] == 'X' and get_list[5] == 'X') or (get_list[3] == 'O' and get_list[4] == 'O' and get_list[5] == 'O'):
        print(msg)
        return True
    elif (get_list[6] == 'X' and get_list[7] == 'X' and get_list[8] == 'X') or (get_list[6] == 'O' and get_list[7] == 'O' and get_list[8] == 'O'):
        print(msg)
        return True
    elif (get_list[0] == 'X' and get_list[3] == 'X' and get_list[6] == 'X') or (get_list[0] == 'O' and get_list[3] == 'O' and get_list[6] == 'O'):
        print(msg)
        return True
    elif (get_list[1] == 'X' and get_list[4] == 'X' and get_list[7] == 'X') or (get_list[1] == 'O' and get_list[4] == 'O' and get_list[7] == 'O'):
        print(msg)
        return True
    elif (get_list[2] == 'X' and get_list[5] == 'X' and get_list[8] == 'X') or (get_list[2 == 'O'] and get_list[5] == 'O' and get_list[8] == 'O'):
        print(msg)
        return True
    elif (get_list[0] == 'X' and get_list[4] == 'X' and get_list[8] == 'X') or (get_list[0] == 'O' and get_list[4] == 'O' and get_list[8] == 'O'):
        print(msg)
        return True
    elif (get_list[2] == 'X' and get_list[4] == 'X' and get_list[6] == 'X') or (get_list[2] == 'O' and get_list[4] == 'O' and get_list[6] == 'O'):
        print(msg)
        return True
    else:
        return False
    
if __name__ == "__main__":
    main()

