# scrabble_cheater
Run word_generator.py to use the script

This repo was made for fun and for practice! It also was made out of necessity, as I kept losing games of scrabble.

In a nutshell, given letters as an inputs, this code tries to find valid scrabble words using edit transducers, scores the words, and tells you what other letters you'd need to form the new word.

See an example below:

Enter your scrabble letters.

Enter blank tiles as 0, if applicable:

\>\>\>zhijk0o

Possible Words:

Word: KOJI      Base Score (without blanks): 15    Needs Letters: {}
Word: ZOO       Base Score (without blanks): 12    Needs Letters: {'O': 1}
Word: KOOK      Base Score (without blanks): 12    Needs Letters: {'K': 1, 'O': 1}
Word: HOOK      Base Score (without blanks): 11    Needs Letters: {'O': 1}
Word: KHI       Base Score (without blanks): 10    Needs Letters: {}
Word: JO        Base Score (without blanks): 9     Needs Letters: {}
Word: KOI       Base Score (without blanks): 7     Needs Letters: {}
Word: KI        Base Score (without blanks): 6     Needs Letters: {}
Word: OOH       Base Score (without blanks): 6     Needs Letters: {'O': 1}
Word: OHO       Base Score (without blanks): 6     Needs Letters: {'O': 1}
Word: HI        Base Score (without blanks): 5     Needs Letters: {}
Word: HO        Base Score (without blanks): 5     Needs Letters: {}
Word: OH        Base Score (without blanks): 5     Needs Letters: {}
Word: OI        Base Score (without blanks): 2     Needs Letters: {}

Note that this code requires pynini, installation instructions here: https://pypi.org/project/pynini/
