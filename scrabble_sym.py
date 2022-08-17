import pynini


class ScrabbleSym(object):
    """parent class for storing some values. Probably overkill"""
    sym_file = 'data/dict.sym'
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
        self.sym = pynini.SymbolTable.read_text(self.sym_file)
        self.sym_fst = self._make_sym_fst(self.sym)

    def _make_sym_fst(self, sym):
        """makes a fst out of a symbol table"""
        sym_iter = iter(sym)
        lex = [pynini.escape(symbol) for _, symbol in sym_iter]
        return pynini.string_map(lex).optimize()

