# cant use function because of exec()
monkeys = [{}]
mod = 1
with open('day11.txt') as f:
    for line in f.readlines():
        line = line.strip()
        if line == "":
            monkeys.append({})
            continue;
        if line.startswith("Starting"):
            _,itemsString = line.split(": ")
            items = [int(x) for x in itemsString.split(", ")]
            monkeys[-1]["items"] = items
        elif line.startswith("Operation"):
            _,op = line.split(": ")
            monkeys[-1]["op"] = op
        elif line.startswith("Test"):
            _,_,_,n = line.split(" ")
            mod *= int(n)
            monkeys[-1]["test"] = int(n)
        elif line.startswith("If true"):
            _,_,_,_,_,n = line.split(" ")
            monkeys[-1]["true"] = int(n)
        elif line.startswith("If false"):
            _,_,_,_,_,n = line.split(" ")
            monkeys[-1]["false"] = int(n)

inspect = [0 for _ in range(len(monkeys))]
monkeyCopy = monkeys.copy()
for roundIndex in range(20):
    for monkeyIndex,monkey in enumerate(monkeys):
        while len(monkey["items"]) > 0:
            item = monkey["items"].pop(0)
            inspect[monkeyIndex] += 1
            old = item
            new = 0
            exec(monkey["op"])
            new //= 3
            if new % monkey["test"] == 0:
                monkeys[monkey["true"]]["items"].append(new)
            else:
                monkeys[monkey["false"]]["items"].append(new)

inspect.sort(reverse=True)
print("First star: ", inspect[0]*inspect[1])

inspect = [0 for _ in range(len(monkeys))]
for roundIndex in range(10000):
    for monkeyIndex,monkey in enumerate(monkeys):
        while len(monkey["items"]) > 0:
            item = monkey["items"].pop(0)
            inspect[monkeyIndex] += 1
            old = item % mod
            new = 0
            exec(monkey["op"])
            if new % monkey["test"] == 0:
                monkeys[monkey["true"]]["items"].append(new)
            else:
                monkeys[monkey["false"]]["items"].append(new)

inspect.sort(reverse=True)
print("Second star: ", inspect[0]*inspect[1])