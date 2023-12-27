from aoc import get_input

data = get_input(1).splitlines()

def get_first_and_last_digit(word):
    first_digit = None
    last_digit = None

    for letter in word:
        if letter.isdigit():
            first_digit = int(letter)
            break
    for letter in word[::-1]:
        if letter.isdigit():
            last_digit = int(letter)
            break
    
    return first_digit, last_digit

sum_of_all = 0

for line in data:
    first_digit, last_digit = get_first_and_last_digit(line)
    sum_of_all += first_digit*10 + last_digit

print("Part 1:", sum_of_all)

DIGITS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def get_first_and_last_digit_spelled(word):
    first_digit = [None, None]
    last_digit = [None, None]

    for i, letter in enumerate(word):
        if letter.isdigit():
            first_digit = [i, int(letter)]
            first_digit
            break
    for i, letter in enumerate(word[::-1]):
        if letter.isdigit():
            last_digit = [len(word)-1-i, int(letter)]
            break

    for digit in DIGITS:
        first_idx = word.find(digit)
        last_idx = word.rfind(digit)
        if first_digit[0] is None or first_idx < first_digit[0] and first_idx != -1:
            first_digit = [first_idx, DIGITS[digit]]
        if last_digit[0] is None or last_idx > last_digit[0] and last_idx != -1:
            last_digit = [last_idx, DIGITS[digit]]
    
    return first_digit[1], last_digit[1]

sum_of_all = 0
for line in data:
        first_digit, last_digit = get_first_and_last_digit_spelled(line)
        sum_of_all += first_digit*10 + last_digit

print("Part 2:", sum_of_all)
print(data)