from aoc import get_input

data = get_input(14).splitlines()
# with open('./data/ex_14.txt', 'r') as f:
#     data = f.read().splitlines()
max_dist = 0
time = 2503

def calculate_dist(speed, time_speed, rest, time=2503):
    cycle_time = time_speed + rest
    distance = time // cycle_time * speed * time_speed + min(time % cycle_time, time_speed) * speed
    return distance

for line in data:
    line = line.strip().split()
    speed, time_speed, rest = int(line[3]), int(line[6]), int(line[-2])
    dist = calculate_dist(speed, time_speed, rest)
    max_dist = max(dist, max_dist)

print(max_dist)

bonus_distances = [0 for _ in data]
for i in range(time+1):
    max_dist = 0
    max_index = -1
    for j, line in enumerate(data):
        line = line.strip().split()
        speed, time_speed, rest = int(line[3]), int(line[6]), int(line[-2])
        dist = calculate_dist(speed, time_speed, rest, time=i)
        if dist > max_dist:
            max_dist = dist
            max_index = j
    bonus_distances[max_index] += 1
print(max(bonus_distances))