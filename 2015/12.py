from aoc import get_input
import re
import json

data = get_input(12).strip()
# with open('./data/ex_1.txt', 'r') as f:
#     data = f.read().splitlines()
pattern = r'-?[0-9]+'
nums = re.findall(pattern, data)
sum_all = sum([int(num) for num in nums])
print(sum_all)

def sum_json(x, skip=None):
   if isinstance(x, list):
     return sum([sum_json(v, skip) for v in x])
   elif isinstance(x, dict):
     if skip is not None and (skip in x or skip in x.values()):
        return 0
     else:
        return sum([sum_json(k, skip) + sum_json(v, skip) for k, v in x.items()])
   else:
     try:
        return int(x)
     except Exception:
        return 0
     
print("part 1", sum_json(json.loads(data)))
print("part 2", sum_json(json.loads(data), "red"))