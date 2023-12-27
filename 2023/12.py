from aoc import get_input
import re

data = get_input(12).splitlines()
# with open('./data/ex_12.txt', 'r') as f:
#     data = f.read().splitlines()
characters = []
patterns = []

def generate_combinations(string):
    def replace_question_mark(index, current_string):
        if index == len(current_string):
            combinations.append(current_string)
            return

        if current_string[index] == '?':
            replace_question_mark(index + 1, current_string[:index] + '#' + current_string[index + 1:])
            replace_question_mark(index + 1, current_string[:index] + '.' + current_string[index + 1:])
        else:
            replace_question_mark(index + 1, current_string)

    combinations = []
    replace_question_mark(0, string)
    return combinations

def find_number_of_combinations(chars, pattern):
    pattern_regex = '\.+'.join(['#' if x == 1 else x*'#' if x > 1 else '\.*' for x in pattern])
    pattern_regex = f'\.*{pattern_regex}\.*'
    combinations = generate_combinations(chars)
    combinations = [combination for combination in combinations if combination.count('#') == sum(pattern)]
    matches = [1 if re.match(pattern_regex, combination) else 0 for combination in combinations]
    return sum(matches)

for line in data:
    chars, pattern = line.split(' ')
    pattern = [int(x) for x in pattern.split(',')]
    characters.append(chars)
    patterns.append(pattern)

number_of_combinations = 0
for chars, pattern in zip(characters, patterns):
    number_of_combinations += find_number_of_combinations(chars, pattern)

print(number_of_combinations)