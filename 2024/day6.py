input = open('day6.txt').read().splitlines()
def calc(inp):
    start_point = tuple((i,inp[i].index("^")) for i in range(len(inp)) if "^" in inp[i])[0]
    d = (-1,0)
    dic = {(-1,0):(0,1),(1,0):(0,-1),(0,1):(1,0),(0,-1):(-1,0)}
    p = set()
    p2 = set()
    while True:
        new = (start_point[0] + d[0], start_point[1] + d[1])
        if (new,d) in p2:
            return True,0
        if not (new[0] >= 0 and new[0] < len(inp) and new[1] >= 0 and new[1] < len(inp[0])):
            break
        if inp[new[0]][new[1]] == "#":
            d = dic[d]
        else:
            start_point = new
            p.add(start_point)
            p2.add((start_point,d))
    return False,len(p)
s2 = 0
print("First star: ", calc(input))
for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == ".":
            inp_save = input[i]
            inp_list = list(input[i])
            inp_list[j] = '#'
            input[i] = "".join(x for x in inp_list)
            s2 += calc(input)[0]
            input[i] = inp_save
print("Second star: ", s2)