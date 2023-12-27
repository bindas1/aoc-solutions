from aoc import get_input
import re

data = get_input(12).splitlines()
# with open('./data/ex_12.txt', 'r') as f:
#     data = f.read().splitlines()
characters = []
patterns = []

characters_2 = []
patterns_2 = []

for line in data:
    chars, pattern = line.split(' ')
    pattern = [int(x) for x in pattern.split(',')]
    characters.append(chars[:])
    patterns.append(pattern[:])
    chars = '?'.join([chars for _ in range(5)])
    pattern *= 5
    characters_2.append(chars)
    patterns_2.append(pattern)

# dictionary for memoization (dynamic programming)
cache = {}

def find_number_of_combinations(chars, pattern, pos_chars, pos_pattern, current_len):
    """
    pos_chars: position of the current_len character in the list of characters
    pos_pattern: position of the current_len pattern in the list of patterns
    current_len: current_len length of the # pattern
    """
    key = (pos_chars, pos_pattern, current_len)
    if key in cache:
        return cache[key]
    if pos_chars == len(chars):
        if pos_pattern == len(pattern) and current_len == 0:
            return 1
        elif pos_pattern == len(pattern)-1 and pattern[pos_pattern] == current_len:
            return 1
        else:
            return 0
    # print(pos_pattern, pattern, len(pattern), current_len)
    if pos_pattern > len(pattern) or (pos_pattern < len(pattern) and current_len > pattern[pos_pattern]):
        cache[key] = 0
        return 0
    
    combinations = 0
    for character in ['.', '#']:
        if chars[pos_chars] == character or chars[pos_chars] == '?':
            if character == '.' and current_len == 0:
                combinations += find_number_of_combinations(chars, pattern, pos_chars+1, pos_pattern, 0)
            elif character == '.' and current_len>0 and pos_pattern<len(pattern) and pattern[pos_pattern]==current_len:
                combinations += find_number_of_combinations(chars, pattern, pos_chars+1, pos_pattern+1, 0)
            elif character == '#':
                combinations += find_number_of_combinations(chars, pattern, pos_chars+1, pos_pattern, current_len+1)
    cache[key] = combinations
    return combinations

number_of_combinations = 0
for chars, pattern in zip(characters, patterns):
    cache.clear()
    number_of_combinations += find_number_of_combinations(chars, pattern, 0, 0, 0)
print(number_of_combinations)

number_of_combinations = 0
for chars, pattern in zip(characters_2, patterns_2):
    cache.clear()
    number_of_combinations += find_number_of_combinations(chars, pattern, 0, 0, 0)
print(number_of_combinations)