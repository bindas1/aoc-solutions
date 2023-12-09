from aoc import get_input

data = get_input(9).splitlines()

def get_next_row_and_prediction(line):
    diff = line[1] - line[0]
    diffs = [diff]
    for num1, num2 in zip(line[1:-1], line[2:]):
        diff = num2 - num1
        diffs.append(diff)
    return line[-1], diffs

sum_of_preds = 0
for line in data:
    next_value, diffs = get_next_row_and_prediction([int(num) for num in line.split(' ')])
    sum_of_preds += next_value + diffs[-1]

    while any(diffs):
        next_value, diffs = get_next_row_and_prediction(diffs)
        sum_of_preds += diffs[-1]

print(sum_of_preds)

# Part 2
sum_of_preds = 0
for line in data:
    nums = [int(num) for num in line.split(' ')]
    _, diffs = get_next_row_and_prediction(nums)
    sum_of_preds += nums[0]

    diffs_first_digits = [diffs[0]]
    while any(diffs):
        next_value, diffs = get_next_row_and_prediction(diffs)
        diffs_first_digits.append(diffs[0])
    
    substract_from_first = 0
    for num in diffs_first_digits[::-1]:
        substract_from_first = num - substract_from_first
    
    sum_of_preds -= substract_from_first


print(sum_of_preds)