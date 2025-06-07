from aoc import get_input
from typing import List

data = get_input(4).splitlines()

valid_passphrases = 0
for line in data:
    words = line.split()
    valid_passphrases += len(set(words)) == len(words)
print(valid_passphrases)

def serialize(words: List[str]) -> List[str]:
    serialized_words = []
    for word in words:
        serialized_parts = []
        word = sorted(word)
        prev, char_counter = None, 0
        for letter in word:
            if letter == prev:
                char_counter += 1
            else:
                serialized_parts.append(f'{prev}{str(char_counter)}')
                prev = letter
        serialized_words.append(''.join(serialized_parts))
    return serialized_words

valid_passphrases = 0
for line in data:
    words = line.split()
    valid_passphrases += len(set(serialize(words))) == len(words)
print(valid_passphrases)
