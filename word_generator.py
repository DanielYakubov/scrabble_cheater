import pynini
from pynini.lib import edit_transducer
from word_checker import WordChecker

from collections import Counter
from typing import List, Tuple
from string import ascii_uppercase
from scrabble_sym import ScrabbleSym


class WordGenerator(ScrabbleSym):
    """Class that is designed to generate scrabble words and validate them"""
    def __init__(self):
        super().__init__()
        self.sigma_star = pynini.union(*ascii_uppercase).star
        self.word_checker = WordChecker()

    def get_possible_words(self, letters: str, blanks=0) -> List[str]:
        """given a combination of letters represented as a str, a list of possible words in the scrabble dictionary
        is returned. The words are all within n-edits, where n is the amount of letters"""
        ET = edit_transducer.EditTransducer(letters.upper(),
                                            bound=len(letters))
        combinations = ET.create_lattice(letters, self.sigma_star).optimize()
        words = set()
        for w in (combinations @ self.sym_fst).paths().ostrings():
            words.add(w)
        return [word for word in words if self.word_checker.possible_in_default_scrabble(word, blank_threshold=blanks)]

    def get_scores(self, word_list: List[str]) -> List[Tuple]:
        """scores each entry in the list based on letter-tile scores. Note that this does not take board configuration
        into account"""
        words_with_scores = {}
        for word in word_list:
            words_with_scores[word] = self.word_checker.calculate_base_word_score(word)
        return sorted(words_with_scores.items(), key=lambda x: x[1], reverse=True)

    @staticmethod
    def get_additional_letters(word: str, letters: str) -> dict:
        """checks if a generated word uses letters that aren't present in the letters param
        then, returns those letters and their frequency"""
        word_letters_counts = Counter(word)
        letters_counts = Counter(letters)

        additional_letters = {}
        for let, count in word_letters_counts.items():
            if letters_counts.get(let, None):
                if letters_counts[let] < word_letters_counts[let]:
                    additional_letters[let] = word_letters_counts[let] - letters_counts[let]
            else:
                additional_letters[let] = word_letters_counts[let]
        return additional_letters

    @staticmethod
    def print_words(words_with_scores: List[str], user_input: str) -> None:
        """displays the words: scores in stdin to the user"""
        wg = WordGenerator()
        print("Possible words:")
        for word, score in words_with_scores:
            print(f"Word: {word:<9} Base Score (without blanks): {score:<5} Needs Letters: {wg.get_additional_letters(word, user_input)}")

    def validate_input(self, letters: str) -> bool:
        if len(letters) > 7:
            return False
        elif set(letters).difference(set(ascii_uppercase + "0")): # any OOV letters?
            return False
        elif not self.word_checker.possible_in_default_scrabble(letters):
            return False
        return True


if __name__ == '__main__':
    wg = WordGenerator()
    user_input = input('Enter your scrabble letters.\n'
                       'Enter blank tiles as 0, if applicable:\n'
                       '>>>').upper()
    while not wg.validate_input(user_input):
        user_input = input('Please enter a valid scrabble combination that fulfills these requirements:\n'
                           '1. Consists of letters and 0s only\n'
                           '2. 7 or less tiles\n'
                           '3. The letters are possible with scrabble\'s tile frequency distribution\n'
                           '4. Letters are English\n'
                           '>>>').upper()
    blanks = user_input.count('0')
    word_list = wg.get_possible_words(user_input, blanks=blanks)
    word_list_with_scores = wg.get_scores(word_list)
    wg.print_words(word_list_with_scores, user_input)