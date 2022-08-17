from collections import Counter

sym_file = 'data/dict.txt'
outfile = 'data.preprocessed_data.txt'

tile_dist = {
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
with open(sym_file) as raw_data:
    with open(outfile, 'w') as dump:
        for line in raw_data:
            line = line.strip()
            letters_in_word = Counter(line)
            is_valid = True
            for let, cnt in letters_in_word.items():
                if tile_dist[let] < cnt:
                    is_valid = False
            if is_valid:
                print(line, file=dump)