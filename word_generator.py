import pynini
from pynini.lib import edit_transducer
from word_checker import WordChecker

from typing import List, Tuple
from string import ascii_uppercase

sym_file = 'data/dict.sym'


class WordGenerator(object):
    def __init__(self):
        self.sym = pynini.SymbolTable.read_text(sym_file)  # todo avoid loading in twice
        self.sym_fst = self._make_sym_fst(self.sym)
        self.sigma_star = pynini.union(*ascii_uppercase).star
        self.wordchecker = WordChecker()

    def _make_sym_fst(self, sym):
        sym_iter = iter(sym)
        lex = [pynini.escape(symbol) for _, symbol in sym_iter]
        return pynini.string_map(lex).optimize()

    def get_possible_words(self, word: str) -> List[str]:
        ET = edit_transducer.EditTransducer(word.upper(),
                                            bound=len(word))
        combinations = ET.create_lattice(word, self.sigma_star).optimize()
        words = set()
        for w in (combinations @ self.sym_fst).paths().ostrings():
            words.add(w)
        return list(words)

    def get_scores(self, word_list: List[str]) -> List[Tuple]:
        words_with_scores = {}
        for word in word_list:
            words_with_scores[word] = self.wordchecker.calculate_base_word_score(word)
        return sorted(words_with_scores.items(), key=lambda x: x[1], reverse=True)

    def print_words(self, words_with_scores: List[str]) -> None:
        for word, score in words_with_scores:
            print(f"Word: {word:<10} Score: {score:<2}")


if __name__ == '__main__':
    wg = WordGenerator()
    word_list = wg.get_possible_words('EEUJZQS')
    word_list_with_scores = wg.get_scores(word_list)
    wg.print_words(word_list_with_scores)
