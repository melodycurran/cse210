from game.terminal_service import TerminalService
# from game.word import Word

class Guesser:
    """The person who guesses the random word letter by letter.
    
    The responsibility of the guesser is to guess the word letter by letter.

    Attributes:
        word (str): The random word from the list
    """

    def __init__(self):
        """Constructs a new Guesser.

        Args:
            self (Guesser): An instance of Guesser.
        """
        # self.get_word = Word()
        self.terminal = TerminalService()
        self.input = ""
        # self.guess_is_right = True

    def _get_input(self):

        self.input = self.terminal.read_text('Guess a letter [a-z]: ')

    # def _evaluate_input(self):
    #     """Evaluates input of the user.

    #     Args:
    #         self (Guesser): An instance of Guesser.
    #     """
        
    #     if self.input in self.word:
    #         self.guess_is_right
    #     else:
    #         not self.guess_is_right


        
