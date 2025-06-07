from aoc import get_input

data = get_input(3).splitlines()
num = int(data[0])

ring = 3
while (ring ** 2 < num):
    ring += 2
# coordinates of the right down item
x, y = ring // 2, ring // 2
# (ring - 1) is the number of steps in a length
# then we take abs to calculate the dist from any middle point
print(ring // 2 + (abs((ring**2 - num) % (ring - 1) - ring // 2 )))


# second solution to part 1 that is easier to understand
# Find the layer of the spiral where the number lies
layer = 0
while (2 * layer + 1) ** 2 < num:
    layer += 1

side_length = 2 * layer + 1
max_value_in_layer = side_length ** 2
steps_per_side = side_length - 1

# Find the closest midpoint of the side to the number
# There are 4 midpoints, one per side
midpoints = [
    max_value_in_layer - layer - steps_per_side * i
    for i in range(4)
]

# Distance is the layer count (steps to get to ring)
# plus the distance from the closest midpoint
min_steps_from_midpoint = min(abs(num - m) for m in midpoints)
distance = layer + min_steps_from_midpoint

print(distance)

# Part 2
# Find first value that is larger than num
pos_x, pos_y = 0, 0
grid = {(0, 0): 1}

def get_value(x, y):
    # Get the sum of all adjacent values that were already calculated
    sum_adjacent = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            sum_adjacent += grid.get((x + dx, y + dy), 0)
    return sum_adjacent

def next_position_generator():
    # The movements go like this - right, up, left, left, down, down, right, right, right
    # We increase the step size after every two turns
    x, y = 0, 0

    directions = [
        (1, 0),  # right
        (0, -1), # up
        (-1, 0), # left
        (0, 1)   # down
    ]
    step_size = 1
    direction = 0

    while True:
        # Increment step size every two iterations
        for _ in range(2):
            dx, dy = directions[direction]
            for _ in range(step_size):
                x, y = x + dx, y + dy
                yield x, y
            direction = (direction + 1) % 4
        step_size += 1

gen = next_position_generator()
while True:
    pos_x, pos_y = next(gen)
    curr_val = get_value(pos_x, pos_y)
    grid[(pos_x, pos_y)] = curr_val
    
    if curr_val > num:
        break

print(curr_val)
