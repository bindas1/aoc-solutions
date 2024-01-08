from aoc import get_input

data = get_input(8).splitlines()
# with open('./data/ex_1.txt', 'r') as f:
#     data = f.read().splitlines()

def num_chars_in_memory(line):
    num_chars = len(line)
    num_chars_in_memory = 0
    i = 0
    previous_backslash = False
    while i < num_chars:
        if line[i] in ['\\', '"'] and previous_backslash:
            num_chars_in_memory += 1
            previous_backslash = False
        elif line[i] == 'x' and previous_backslash:
            i += 2
            num_chars_in_memory += 1
            previous_backslash = False
        elif line[i] == "\\":
            previous_backslash = True
        else:
            num_chars_in_memory += 1
        i += 1
    return num_chars_in_memory

total = 0
for line in data:
    num_chars = len(line)
    total += num_chars - num_chars_in_memory(line[1:-1])
print("part 1", total)

def num_chars_in_encoded_line(line):
    num_chars = len(line)
    # + 6 comes from two apostrophe in the beg and end i.e. "\"...\""
    num_chars_in_encoding = 6
    i = 0
    previous_backslash = False
    while i < num_chars:
        if line[i] in ['\\', '"'] and previous_backslash:
            num_chars_in_encoding += 4
            previous_backslash = False
        elif line[i] == 'x' and previous_backslash:
            i += 2
            num_chars_in_encoding += 5
            previous_backslash = False
        elif line[i] == "\\":
            previous_backslash = True
        else:
            num_chars_in_encoding += 1
        i += 1
    return num_chars_in_encoding

total = 0
for line in data:
    num_chars = len(line)
    total +=  - num_chars + num_chars_in_encoded_line(line[1:-1])
print("part 2", total)