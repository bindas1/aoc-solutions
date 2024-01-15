from aoc import get_input
import re
import random

transitions, sequence = get_input(19).split('\n\n')
transitions = transitions.splitlines()
# with open('./data/ex_1.txt', 'r') as f:
#     data = f.read().splitlines()
swaps = {}
molecules = set()

def create_molecules(sequence, initial, final):
    indices = [m.start() for m in re.finditer(initial, sequence)]
    len_initial = len(initial)
    new_molecules = [sequence[:i] + final + sequence[i+len_initial:] for i in indices]
    return new_molecules

for line in transitions:
    initial, final = line.split(' => ')
    new_molecules = create_molecules(sequence, initial, final)
    for molecule in new_molecules:
        molecules.add(molecule)
    swaps[final] = initial

# part 1
print(len(molecules))

current_molecule = sequence
steps = 0
modified = True
keys_sample = list(swaps.keys())
random.shuffle(keys_sample)

while current_molecule != 'e':
    modified = False
    for key in keys_sample:
        initial = swaps[key]
        
        if key in current_molecule:
            current_molecule = current_molecule.replace(key, initial, 1)
            steps += 1
            modified = True

    if not modified:
        current_molecule = sequence
        random.shuffle(keys_sample)
        steps = 0

    # print(current_molecule)
# part 2
print(steps)

# part 2 different solution from other repo (modified it to working with shuffling)
def retrosynthesis(target_groups: dict, target_molecule: str) -> list:
    current_molecule = target_molecule
    steps = 0
    items = list(target_groups.items())
    random.shuffle(items)

    # start by doing all the substitions, without e
    # repeat until the molecule is not modified
    molecule_modified = True
    while molecule_modified:
        molecule_modified = False

        for tgt_grp, src_grp in items:
            if src_grp == 'e':
                continue

            # count how many matches of target first
            substitutions = current_molecule.count(tgt_grp)

            # then replace them all
            if substitutions > 0:
                current_molecule = current_molecule.replace(tgt_grp, src_grp)
                molecule_modified = True
                steps += substitutions

    # now replace target with e
    for tgt_grp, src_grp in items:
        if src_grp != 'e':
            continue

        # count how many matches of target first
        substitutions = current_molecule.count(tgt_grp)

        # then replace them all
        if substitutions > 0:
            current_molecule = current_molecule.replace(tgt_grp, src_grp)
            steps += substitutions
    return current_molecule, steps

current_molecule = None
while current_molecule != 'e':
    current_molecule, steps = retrosynthesis(swaps, sequence)
print(steps)