import ast
from functools import cmp_to_key
def compare(first, second):
    if type(first) == int and type(second) == int:
        return 0 if first == second else 1 if first < second else -1
    elif type(first) == list and type(second) == list:
        for i in range(min(len(first), len(second))):
            c = compare(first[i], second[i])
            if c:
                return c
        return 0 if len(first) == len(second) else 1 if len(first) < len(second) else -1
    elif type(first) == int and type(second) == list:
        return compare([first], second)
    elif type(first) == list and type(second) == int:
        return compare(first, [second])
with open('day13.txt') as f:
    inp = [x for x in f.read().split("\n\n")]
val = [(ast.literal_eval(x),ast.literal_eval(y)) for x,y in (z.split("\n") for z in inp)]
val2 = []
for x in inp:
    first, second = x.split("\n")
    val2.append(ast.literal_eval(first))
    val2.append(ast.literal_eval(second))
val2.append([2])
val2.append([6])
val2.sort(key=cmp_to_key(compare), reverse=True)
print("First star: ", sum(i+1 for i,(x,y) in enumerate(val) if compare(x,y) == 1))
print("Second star: ", (val2.index([2])+1) * (val2.index([6])+1))