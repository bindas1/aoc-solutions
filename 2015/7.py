from aoc import get_input


data = get_input(7).splitlines()
# with open('./data/ex_7.txt', 'r') as f:
#     data = f.read().splitlines()

wires = {}

calculations = {}
results = {}

def calculate(name, results):
    if name.isnumeric():
        return int(name)
    else:
        if name not in results:
            operation = calculations[name]
            if len(operation) == 1:
                results[name] = calculate(operation[0], results)
            elif operation[0] == "NOT":
                results[name] = ~calculate(operation[1], results) & 0xFFFF
            else:
                left, gate, right = operation
                if gate == "AND":
                    results[name] = calculate(left, results) & calculate(right, results)
                elif gate == "OR":
                    results[name] = calculate(left, results) | calculate(right, results)
                elif gate == "LSHIFT":
                    results[name] = calculate(left, results) << int(right)
                elif gate == "RSHIFT":
                    results[name] = calculate(left, results) >> int(right)
                else:
                    assert False, f"Unknown gate, {left, gate, right}"
        return results[name]

for line in data:
    input, output = line.split(' -> ')
    calculations[output.strip()] = input.strip().split(' ')
print(calculate('a', results))

results_2 = {}
results_2['b'] = results['a']
print(calculate('a', results_2))