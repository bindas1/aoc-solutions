from aoc import get_input

data = [int(elem.split(': ')[1]) for elem in get_input(21).splitlines()]

boss_hitpoints = data[0]
boss_dmg = data[1]
boss_armor = data[2]
boss = [boss_hitpoints, boss_dmg, boss_armor]

my_hitpoints = 100
my_dmg = 0
my_armor = 0

weapons = {
    'Dagger': [8, 4, 0],
    'Shortsword': [10, 5, 0],
    'Warhammer': [25, 6, 0],
    'Longsword': [40, 7, 0],
    'Greataxe': [74, 8, 0],
}

armors = {
    'Leather': [13, 0, 1],
    'Chainmail': [31, 0, 2],
    'Splintmail': [53, 0, 3],
    'Bandedmail': [75, 0, 4],
    'Platemail': [102, 0, 5],
    'None': [0, 0, 0],
}

rings = {
    'Damage +1': [25, 1, 0],
    'Damage +2': [50, 2, 0],
    'Damage +3': [100, 3, 0],
    'Defense +1': [20, 0, 1],
    'Defense +2': [40, 0, 2],
    'Defense +3': [80, 0, 3],
    'None': [0, 0, 0],
}

def simulate_game(player, boss):
    boss = boss[:]
    while True:
        boss[0] -= max(1, player[1] - boss[2])
        if boss[0] <= 0:
            return True
        player[0] -= max(1, boss[1] - player[2])
        if player[0] <= 0:
            return False
        
min_cost = 1000000
possibilities = {}
for weapon in weapons:
    for armor in armors:
        for ring1 in rings:
            for ring2 in rings:
                if ring1 == ring2 and ring1 != 'None':
                    continue
                player = [my_hitpoints, my_dmg, my_armor]
                player[1] += weapons[weapon][1]
                player[2] += armors[armor][2]
                player[1] += rings[ring1][1]
                player[2] += rings[ring1][2]
                player[1] += rings[ring2][1]
                player[2] += rings[ring2][2]
                cost = weapons[weapon][0] + armors[armor][0] + rings[ring1][0] + rings[ring2][0]
                if simulate_game(player, boss):
                    min_cost = min(min_cost, cost)
                    possibilities[cost] = [weapon, armor, ring1, ring2]
print(min_cost)
print(possibilities[min_cost])

max_cost = 0
for weapon in weapons:
    for armor in armors:
        for ring1 in rings:
            for ring2 in rings:
                if ring1 == ring2 and ring1 != 'None':
                    continue
                player = [my_hitpoints, my_dmg, my_armor]
                player[1] += weapons[weapon][1]
                player[2] += armors[armor][2]
                player[1] += rings[ring1][1]
                player[2] += rings[ring1][2]
                player[1] += rings[ring2][1]
                player[2] += rings[ring2][2]
                cost = weapons[weapon][0] + armors[armor][0] + rings[ring1][0] + rings[ring2][0]
                if not simulate_game(player, boss):
                    max_cost = max(max_cost, cost)
                    possibilities[cost] = [weapon, armor, ring1, ring2]
print(max_cost)
print(possibilities[max_cost])