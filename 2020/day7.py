d = {}
def part1(x):
    if x == False:
        return False
    else:
        for y in x:
            if y[0] == "shiny gold":
                return True
            elif part1(d[y[0]]):
                return True
    return False
def part2(x):
    count = 0
    if x == False:
        return 0
    else:
        for y in x:
            count += y[1]
            i = part2(d[y[0]])
            count += y[1]*i
    return count
with open('day7.txt') as f:
    for line in f.readlines():
        splitted = line.strip().split(" ")
        name = splitted[0] + " " + splitted[1]
        if splitted[4] == "no":
            d[name] = False
        else:
            i = 3
            first = True
            d[name] = []
            while first or splitted[i].endswith(","):
                i+=4
                name2 = splitted[i-2] + " " + splitted[i-1]
                d[name].append((name2,int(splitted[i-3])))
                first = False
ans = 0
for x in d.values():
    ans += part1(x)
print("First star: ", ans)
print("Second star: ", part2(d["shiny gold"]))