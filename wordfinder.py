"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder:
    """
    
    Attributes
    ----------
    file:
    path to the file containing the list of words


    """
    def __init__(self, filename):
        self.filename = filename

        # get wordlist
        word_file = open(self.filename)
        self.word_list = self.get_word_list(word_file)
        self.num_words = len(self.word_list)
        self.read_words()


    def read_words(self):
        return print(f"{self.num_words} words read.")

    def get_word_list(self, word_file):
        return [w.strip() for w in word_file]


    def random(self):
        return choice(self.word_list)
    

class RandomWordFinder(WordFinder):
    """Generates a random word from a text file list, but removes blank lines and #commented lines from the original text file
    
    Attributes:

    file:
    txt file containing a list of randomly generated words
    
    """
    def __init__(self, filename):
        super().__init__(filename)

    def get_word_list(self, word_file):
    
        return [w.strip() for w in word_file
                if w.strip() and not w.startswith("#")]