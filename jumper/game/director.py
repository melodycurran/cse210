from game.word import Word
from game.terminal_service import TerminalService
from game.guesser import Guesser

class Director:
    """The person who directs the game.
    
    Attributes:

        _draw_parachute(str): Draws the parachute
        _is_playing(boolean): Directs the loop of the game
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._random_word = Word()
        self._terminal = TerminalService()
        self.guesser = Guesser()
        self.parachute = []
        self.msg = ""
        self.hide = ""
        self.wrong_guess = []
        self.word = ""


    def _start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_random_word()
            self._hide_word()
            self._draw_parachute()
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_random_word(self):
        """Generate random word and hide it from the player.
        
        Args:
            self (Director): an instance of Director.
        """
        self.word = self._random_word.get_word()

    def _hide_word(self):

        guess = self.guesser.input
        
        if guess == "":
            self.hide = "_" * len(self.word)
            self._terminal.write_text(f'The word is: {self.hide}')
        
        elif guess in self.word:
            i = self.word.index(guess)

            self.hide = self.hide[:i] + self.word[i] + self.hide[i + 1:]
            self._terminal.write_text(f'The word is: {self.hide}')

        else:
            self._terminal.write_text(f'The word is: {self.hide}')

    def _draw_parachute(self):
        """Prints the parachute on the terminal.
        
        Args:
            self (Director): an instance of Director
        """
        self.parachute = [
            '   _____',
            '  /_____\\',
            '  \     /',
            '   \   /',
            '     0',
            '    /|\\',
            '    / \\',
            '',
            ' ^^^^^^^^^^'
        ]

        for line in self.parachute:
            self._terminal.write_text(line)

    def _get_inputs(self):
        """Get input from the user about their guess.

        Args:
            self (Director): An instance of Director.
        """
        if self.hide != self.word:
            self.guesser._get_input()

    def _do_updates(self):
        """Updates when the player guesses the letter right or not.

        Args:
            self (Director): An instance of Director.
        """
        if self.guesser.input in self.word:
            pass

        else:
            self.wrong_guess.append(self.guesser.input)

            for count in range(0, len(self.wrong_guess)):
                if count == 4:
                    self.parachute[0] = '     X'
                    self._terminal.write_text('Game is over!')
                    return
                else:
                    self.parachute.pop(0)
                

    def _do_outputs(self):

        if self.hide == self.word:
            not self._is_playing
            self._terminal.write_text('Game is over!')
            return

