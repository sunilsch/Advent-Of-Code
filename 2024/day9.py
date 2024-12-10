inp = [(int(x),i//2 if i % 2 == 0 else "") for i,x in enumerate(open('day9.txt').readline())]
inp2 = inp.copy()
def calcRes(_inp):
    s, blocks = 0,0
    for x in _inp:
        for _ in range(x[0]):
            if x[1] != "":
                s += blocks*x[1]
            blocks += 1
    return s
def part1():
    i = 1
    while i < len(inp):
        space = inp[i][0]
        c = 0
        while c < space:
            right = inp[-1]
            if right[1] == '':
                inp.pop()
                continue
            if c+right[0] <= space:
                inp.insert(i,right)
                inp.pop()
                i += 1
                c += right[0]
            else:
                inp.insert(i, (space-c, right[1]))
                inp[-1] = (right[0]-(space-c),right[1])
                i += 1
                break
        inp.pop(i)
        i += 1
def part2():
    j = 1
    while j < len(inp2):
        right = inp2[-j]
        if inp2[-j][1] == '':
            j+=1
            continue
        i = 0
        while i < len(inp2)-j:
            if inp2[i][1] != '':
                i += 1
                continue
            if inp2[i][0] >= right[0]:
                inp2.insert(i, right)
                inp2[-j] = (inp2[-j][0],"")
                i += 1
                inp2[i] = (inp2[i][0]-right[0],"")
                break
            i += 1
        j+=1
part1()
part2()
print("First star: ", calcRes(inp))
print("Second star: ", calcRes(inp2))