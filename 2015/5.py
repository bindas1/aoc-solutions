from aoc import get_input

data = get_input(5).splitlines()
# with open('./data/ex_1.txt', 'r') as f:
#     data = f.read().splitlines()

def is_nice(line):
    vowels = 'aeiou'
    bad_strings = ['ab', 'cd', 'pq', 'xy']
    count_vowels = 0
    has_duplicates = False

    for i in range(len(line)-1):
        substring = line[i:i+2]
        if substring in bad_strings:
            return False
        if not has_duplicates:
            if substring[0] == substring[1]:
                has_duplicates = True
        if line[i] in vowels:
            count_vowels += 1
    if line[-1] in vowels:
        count_vowels += 1
        
    if count_vowels >= 3 and has_duplicates:
        return True
    else:
        return False
    
def is_nice_2(line):
    contains_duplicate_substring = False

    for i in range(len(line)-1):
        substring = line[i:i+2]
        if substring in line[:i] or substring in line[i+2:]:
            contains_duplicate_substring = True
            break
    
    if not contains_duplicate_substring:
        return False
    
    for i in range(len(line)-2):
        substring = line[i:i+3]
        if substring[0] == substring[-1]:
            return True
        
    return False

nice_lines = 0
for line in data:
    nice_lines += 1 if is_nice(line) else 0
print(nice_lines)

nice_lines = 0
for line in data:
    nice_lines += 1 if is_nice_2(line) else 0
print(nice_lines)
