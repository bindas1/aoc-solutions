from aoc import get_input

data = get_input(16).splitlines()
# with open('./data/ex_1.txt', 'r') as f:
#     data = f.read().splitlines()

ground_truth = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

sues = []

for line in data:
    line = line.replace(',', '').replace(':', '').split()
    sue = {}
    for i in range(2, len(line), 2):
        sue[line[i]] = int(line[i+1])
    sues.append(sue)

first_sues = [(i+1, sue) for i, sue in enumerate(sues) if all(sue[key] == ground_truth[key] for key in sue)]
print(first_sues[0])

greater_than = ["cats", "trees"]
fewer_than = ["pomeranians", "goldfish"]
equal_to = [key for key in ground_truth if key not in greater_than and key not in fewer_than]
for i, sue in enumerate(sues):
    all_true = True
    for key in sue:
        if key in greater_than:
            if sue[key] <= ground_truth[key]:
                all_true = False
                break
        elif key in fewer_than:
            if sue[key] >= ground_truth[key]:
                all_true = False
                break
        else:
            if sue[key] != ground_truth[key]:
                all_true = False
                break
    if all_true:
        print(i+1, sue)
        break