import operator
from collections import defaultdict
from aoc import get_input

data = get_input(8).splitlines()
vals = defaultdict(int)


def evaluates_to_true(statement: str) -> bool:
    variable, oper, num = statement.split()
    operators = {
        "==": operator.eq,
        "!=": operator.ne,
        "<": operator.lt,
        "<=": operator.le,
        ">": operator.gt,
        ">=": operator.ge,
    }
    return operators[oper](vals[variable], int(num))


def execute(operation: str, current_max_val: int) -> int:
    variable, oper, num = operation.split()
    if oper == "inc":
        vals[variable] += int(num)
        current_max_val = max(current_max_val, vals[variable])
    else:
        vals[variable] -= int(num)
    return current_max_val


max_val_at_any_step = 0
for line in data:
    operation, if_statement = line.split(" if ")

    if evaluates_to_true(if_statement):
        max_val_at_any_step = execute(operation, max_val_at_any_step)
print(max(vals.values()))
print(max_val_at_any_step)
