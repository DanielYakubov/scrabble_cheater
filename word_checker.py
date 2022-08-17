import pynini
from scrabble_sym import ScrabbleSym


class WordChecker(ScrabbleSym):
    """creates an object that uses a fst symbol table to check if a word is valid in scrabble, and scores it"""

    def __init__(self):
        super().__init__()

    def is_valid_scrabble_word(self, word: str) -> bool:
        """checks if the param word is a valid word in the scrabble dictionary"""
        return self.sym.member(word.upper())

    @classmethod
    def calculate_base_word_score(cls, word: str) -> int:
        """calculated the score of the word using scrabble letter scores"""
        return sum([cls.letter_to_point_val[let] for let in word.upper()])


if __name__ == '__main__':
    wc = WordChecker()
    word = 'hack'
    assert wc.is_valid_scrabble_word(word) is True
    assert wc.calculate_base_word_score(word) == 13
