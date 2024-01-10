from aoc import get_input
import time

password = get_input(11).strip()
# with open('./data/ex_1.txt', 'r') as f:
#     data = f.read().splitlines()

def get_new_possibility(password):
    new_pass = ''
    for i, character in enumerate(password[::-1]):
        if character == 'z':
            new_pass += 'a'
        else:
            new_pass += chr(ord(character) + 1)
            if i+1 < len(password):
                new_pass += password[::-1][i+1:]
            break
    return new_pass[::-1]

def is_valid(password):
    overlaping_pairs = set()
    consecutive_triple = False
    len_pass = len(password)
    
    for i, character in enumerate(password):
        if character in ['i', 'o', 'l']:
            return False
        if i + 1 < len_pass:
            if password[i+1] == character:
                overlaping_pairs.add(character)
        if not consecutive_triple and i + 2 < len_pass:
            if ord(password[i+1])-1 == ord(character) and ord(password[i+1])+1 == ord(password[i+2]):
                consecutive_triple = True

    if len(overlaping_pairs) >= 2 and consecutive_triple:
        return True
    else:
        return False
            

def generate_next(password):
    while True:
        password = get_new_possibility(password)
        if is_valid(password):
            print("Next password: ", password)
            return password

password = generate_next(password)
generate_next(password)