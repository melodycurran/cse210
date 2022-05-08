import random

# 1) Add the class declaration. Use the following class comment.
class Card:
    """Not a graphical card. Will only show its value from 1-13
    The responsibility of Card is to show first and second card value,
    check if player guessed correctly and calculate the points for 
    it.
   
    Attributes:
        value (int): The value of the first card.
        points (int): The number of points the die is worth.
        second_value (int): The value of the second card.
        player_guess (boolean): Whether player guess if the second card value is high or low.
        player_input (str): To ask if player's guess if high or low.
    """

    # 2) Create the class constructor. Use the following method comment.
    def __init__(self):
        """Constructs a new instance of Card with a value and points attribute.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0
        self.second_value = 0 + 1
        self.points = 0
        self.player_guess = True
        self.player_input = ""

    # 3) Create the show_card(self) method. Use the following method comment.
    def show_card(self):
        """Generates a new random value and checks if player guessed correctly.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1,14)

        self.hi_or_lo = input('High or Low? [h/l] ')

        self.player_input == (self.hi_or_lo == 'h' or 'l')

        self.second_value = random.randint(1,14)

        if self.second_value > self.value and self.player_input == 'h':
            self.player_guess = True
        elif self.second_value < self.value and self.player_input == 'l':
            self.player_guess = True
        else:
            self.player_guess = False

    # 3) Create the compute_points(self) method. Use the following method comment.
    def compute_points(self):
        """Computes the points.
        
        Args:
            self (Card): An instance of Card.
        """

        if self.player_guess:
            self.points = 100
        else: 
            self.points = 75
