from aoc import get_input

data = get_input(1)
# with open('./data/ex_1.txt', 'r') as f:
#     data = f.read()

current_dir = 0
horizontal = 0
vertical = 0

directions = {
    'L':-1,
    'R':1
}

locations = set()

moves = data.split(', ')
for move in moves:
    direction = move[0]
    step = int(move[1:]) 
    current_dir = (current_dir + directions[direction]) % 4

    match current_dir:
        case 0:
            for i in range(step):
                if (horizontal, vertical) in locations:
                    break
                locations.add((horizontal, vertical))
                vertical += 1
        case 1:
            for i in range(step):
                if (horizontal, vertical) in locations:
                    break
                locations.add((horizontal, vertical))
                horizontal += 1
        case 2:
            for i in range(step):
                if (horizontal, vertical) in locations:
                    break
                locations.add((horizontal, vertical))
                vertical -= 1
        case 3:
            for i in range(step):
                if (horizontal, vertical) in locations:
                    break
                locations.add((horizontal, vertical))
                horizontal -= 1
    
print(abs(horizontal) + abs(vertical))