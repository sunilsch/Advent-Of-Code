from math import gcd
data = open('day8.txt').read().splitlines()
ins = data[0]
data = data[2:]
d = {}
for line in data:
    f,t = line.replace("(","").replace(")","").split(" = ")
    d[f] = t.split(", ")
def part1():
    c = "AAA"
    s = 0
    i = 0
    while c != "ZZZ":
        if ins[i] == "L":
            c = d[c][0]
        else:
            c = d[c][1]
        i = (i+1) % len(ins)
        s += 1
    return s
def part2():
    c = []
    s = 0
    i = 0
    for x in list(d.keys()):
        if x.endswith("A"):
            c.append(x)
    end = False
    values = [0 for _ in range(len(c))]
    while not end:
        for j,x in enumerate(c):
            if ins[i] == "L":
                c[j] = d[c[j]][0]
            else:
                c[j] = d[c[j]][1]
            if c[j].endswith("Z"):
                values[j] = (s+1)
        i = (i+1) % len(ins)
        s += 1
        end = values.count(0) == 0
    s = 1
    for i in values:
        s = s*i//gcd(s, i)
    return s
print(part1())
print(part2())