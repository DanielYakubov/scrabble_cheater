import pynini

# dictionary from https://github.com/redbo/scrabble/blob/master/dictionary.txt
sym_file = 'data/dict.sym'


class WordChecker(object):
    """creates an object that uses a fst symbol table to check if a word is valid in scrabble, and scores it"""
    letter_to_point_val = {
        '<BLANK>': 0,
        'A': 1,
        'E': 1,
        'I': 1,
        'L': 1,
        'N': 1,
        'O': 1,
        'R': 1,
        'S': 1,
        'T': 1,
        'U': 1,
        'D': 2,
        'G': 2,
        'B': 3,
        'C': 3,
        'M': 3,
        'P': 3,
        'F': 4,
        'H': 4,
        'V': 4,
        'W': 4,
        'Y': 4,
        'K': 5,
        'J': 8,
        'X': 8,
        'Q': 10,
        'Z': 10
    }

    def __init__(self):
        self.sym = pynini.SymbolTable.read_text(sym_file)

    def is_valid_scrabble_word(self, word: str) -> bool:
        return self.sym.member(word)

    @classmethod
    def score_word(cls, word: str) -> int:
        return sum([cls.letter_to_point_val[let] for let in word.upper()])


if __name__ == '__main__':
    wc = WordChecker()
    word = 'hack'
    print(wc.is_valid_scrabble_word(word))
    print(wc.score_word(word))