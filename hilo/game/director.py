from game.cards import Card
import random


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card (List[Card]): A list of Card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play. Inital score is 300
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card = []
        self.is_playing = True
        self.score = 300

        for i in range(1):
            card = Card()
            self.card.append(card)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        # While is_playing is true, execute these functions
        while self.is_playing:           
            self.play_card()
            self.do_outputs()
            # To make sure the game will stop if player reached 0 points
            if self.score <= 0:
                print(f'Game is over!')
                return
            else:
                # If the player has more than 0 points then execute this
                self.get_inputs()

       
    def play_card(self):
        """Show both cards. Lets the player guess and Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        for i in range(len(self.card)):
            card = self.card[i]
            card.card()
        self.score += card.points 


    def do_outputs(self):
        """Displays the score. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        # This line prevents the player from having negative score
        if self.score < 0:
            print(f'Your score is: 0')
        else:
            print(f"Your score is: {self.score}\n")
            self.is_playing == (self.score > 0)
    
    def get_inputs(self):
        """Ask the user if they want to play again.

        Args:
            self (Director): An instance of Director.
        """
        play_again = input("Play again? [y/n] ")
        self.is_playing = (play_again == "y")