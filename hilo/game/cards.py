import random


# TODO: Implement the Card class as follows...

# 1) Add the class declaration. Use the following class comment.
class Card:
    """A card that has values from 1-13. Two cards will show. User has to guess if the second card is 
    higher or lower than the first card before the second card is shown.
    The responsibility of Card is to keep track of cards values, compare if player
    guessed it right and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of first card.
        player_guess (str): Player guess if the second card will be Higher or Lower
        points (int): The number of points player will get for guessing right.
        second_value (int): The value of the second card
    """

# 2) Create the class constructor. Use the following method comment.
    def __init__(self):
        """Constructs a new instance of Card with a value and points attribute.

        Args:
            self (Card): An instance of Card.
        """
        self.points = 0
        self.player_guess = ""
        self.second_value = 0
        self.value = 0

# 3) Create the roll(self) method. Use the following method comment.
    def card(self):
        """Generates a new random value and calculates the points.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1,13)
        print(f'The card is: {self.value}')

        self.player_guess = input("Higher or Lower? [h/l] ")

        self.second_value = random.randint(1,13)

        if self.value == self.second_value:
            self.second_value + random.randint(1,10)
        print(f'The second card is: {self.second_value}')

        if (self.second_value > self.value) and (self.player_guess == 'h'):
            self.points = 100
        elif (self.second_value < self.value) and (self.player_guess == 'l'):
            self.points = 100
        else:
            self.points = -75