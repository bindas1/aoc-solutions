from aoc import get_input
from functools import reduce

data = get_input(15).splitlines()
total_teaspoons = 100
# with open('./data/ex_1.txt', 'r') as f:
#     data = f.read().splitlines()

def calculate_score(combination, exact_calories=None):
    features = [0 for _ in range(4)]
    sum_calories = 0
    for i, ingredient in enumerate(data):
        ingredient = ingredient.split(', ')
        ingredient[0] = ' '.join(ingredient[0].split()[1:])
        ingredient_features = [int(feature.split()[-1]) for feature in ingredient[:-1]]
        sum_calories += int(ingredient[-1].split()[-1]) * combination[i]
        for j, feature in enumerate(ingredient_features):
            features[j] += feature * combination[i]
    features = [max(feature, 0) for feature in features]
    if exact_calories is None or exact_calories == sum_calories:
        return reduce(lambda x,y: x*y, features)
    else:
        return -1

# assuming we have 4 ingredients
def generate_all_combinations():
    for i in range(total_teaspoons+1):
        rest_1 = total_teaspoons - i
        for j in range(rest_1+1):
            rest_2 = rest_1 - j
            for k in range(rest_2+1):
                yield(i, j, k, total_teaspoons-i-j-k)

max_score = 0
best_combination = None
for combination in generate_all_combinations():
    score = calculate_score(combination)
    # max_score = max(score, max_score)
    if score > max_score:
        max_score = score
        best_combination = combination
print(max_score)
print(best_combination)

max_score = 0
best_combination = None
for combination in generate_all_combinations():
    score = calculate_score(combination, 500)
    # max_score = max(score, max_score)
    if score > max_score:
        max_score = score
        best_combination = combination
print(max_score)
print(best_combination)