import pynini


class ScrabbleSym(object):
    """parent class for storing some values. Probably overkill"""
    sym_file = 'data/dict.sym'
    letter_to_point_val = {
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
    tile_dist = {
        "0": 2,
        "A": 9,
        "B": 2,
        "C": 2,
        "D": 4,
        "E": 12,
        "F": 2,
        "G": 3,
        "H": 2,
        "I": 9,
        "J": 1,
        "K": 1,
        "L": 4,
        "M": 2,
        "N": 6,
        "O": 8,
        "P": 2,
        "Q": 1,
        "R": 6,
        "S": 4,
        "T": 6,
        "U": 4,
        "V": 2,
        "W": 2,
        "X": 1,
        "Y": 2,
        "Z": 1
    }

    def __init__(self):
        self.sym = pynini.SymbolTable.read_text(self.sym_file)
        self.sym_fst = self._make_sym_fst(self.sym)

    def _make_sym_fst(self, sym):
        """makes a fst out of a symbol table"""
        sym_iter = iter(sym)
        lex = [pynini.escape(symbol) for _, symbol in sym_iter]
        return pynini.string_map(lex).optimize()

