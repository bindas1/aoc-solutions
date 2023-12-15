from aoc import get_input
from collections import defaultdict

data = get_input(15).split(',')
# with open('./data/ex_15.txt', 'r') as f:
#     data = f.read().split(',')

def hash_algorithm(word):
    current_val = 0
    for char in word:
        current_val += ord(char)
        current_val *= 17
        current_val %= 256
    return current_val

total_sum = 0
for word in data:
    total_sum += hash_algorithm(word)

print("Part 1", total_sum)

boxes = defaultdict(list)
for word in data:
    if '=' in word:
        [label, focal_len] = word.split('=')
        box_num = hash_algorithm(label)
        no_box = True
        for i, label_box in enumerate([box[0] for box in boxes[box_num]]):
            # if there is already a box with the label, update the focal length
            if label_box == label:
                no_box = False
                boxes[box_num][i] = (label, int(focal_len))
        if no_box:
            # otherwise add a new box
            boxes[box_num].append((label, int(focal_len)))
    elif '-' in word:
        [label, _] = word.split('-')
        box_num = hash_algorithm(label)
        # remove the box with the label
        boxes[box_num] = [box for box in boxes[box_num] if box[0] != label]
    else:
        assert "Invalid word {}".format(word)

total_sum = 0
for box_num, box_list in boxes.items():
    for i, box in enumerate(box_list):
        total_sum += (box_num+1) * (i+1) * box[1]
print("Part 2", total_sum)