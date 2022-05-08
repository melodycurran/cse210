from game.cards import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        initial_points: Initial points is automatically set at 300.
        show_card (boolean): Whether or not the player wants to show the card.
        points (int): The points for one round of play.
        total_points (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        
        self.initial_points = 300
        self.show_card = True
        self.points = 0
        self.total_points = 0

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """

        while self.show_card:
            self.show_card_value()
            self.player_input()
            self.update_points()
            self.show_score()

    def show_card_value(self):
        """Ask the user if they want to show card.

        Args:
            self (Director): An instance of Director.
        """

        user_input = ('Do you want to show card? [y/n] ')
        self.show_card = (user_input == 'y')

    def player_input(self):
        """Shows the card and run the show_card method from Card class

        Args:
            self (Director): An instance of Director.
        """
        self.card = Card()
        self.card.show_card()

    def update_points(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """

        self.card = Card()
        if self.card.player_guess == True:
            self.initial_points + self.card.points
    
        else:
            self.initial_points - self.card.points

    def show_score(self):
        """Displays the score. 

        Args:
            self (Director): An instance of Director.
        """

        self.total_points += self.card.points
        print(f'You\'re score is {self.total_points}')
