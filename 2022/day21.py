digitsMonkeys = {}
operationMonkeys = {}
with open('day21.txt') as f:
    for line in f.readlines():
        name, value = line.strip().split(": ")
        if value.isdigit():
            digitsMonkeys[name] = int(value)
        else:
            splitted = tuple(value.split(" "))
            operationMonkeys[name] = splitted
def getValue(monkey,used=False):
    if(monkey == "humn"):
        used = True
    if digitsMonkeys.get(monkey) != None:
        return digitsMonkeys.get(monkey), used
    else:
        value = operationMonkeys[monkey]
        first, usedNew = getValue(value[0],used)
        used = max(used, usedNew)
        second, usedNew = getValue(value[2],used)
        if value[1] == "+":
            v = first + second
        elif value[1] == "-":
            v = first - second
        elif value[1] == "*":
            v = first * second
        else:
            v = first // second
        used = max(used, usedNew)
        return v,used
def part2(monkey, value):
    if(monkey == "humn"):
        print("Second star: ", value)
        exit();
    else:
        op = operationMonkeys[monkey]
        if getValue(op[0])[1] == True:
            v = getValue(op[2])[0]
            if op[1] == "+":
                new = value-v
            elif op[1] == "-":
                new = value+v
            elif op[1] == "*":
                new = value//v
            else:
                new  = value*v
            part2(op[0], new)
        else:
            v = getValue(op[0])[0]
            if op[1] == "+":
                new = value-v
            elif op[1] == "-":
                new = v-value
            elif op[1] == "*":
                new = value//v
            else:
                new = v//value
            part2(op[2], new)
print("First star: ", getValue("root")[0])
rootOneSide = getValue("jntz")
part2("prrg", rootOneSide[0])