with open('day8.txt') as f:
    ins = [x.strip().split(" ") for x in f.readlines()]
c = 0
visited = set()
alive = True
res = 0
while alive:
    if c in visited:
        alive = False
    else:
        visited.add(c)
        if ins[c][0] == "acc":
            res += int(ins[c][1])
            c += 1
        elif ins[c][0] == "jmp":
            c += int(ins[c][1])
        else:
            c += 1
print("First star: ", res)