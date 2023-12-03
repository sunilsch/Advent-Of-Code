comb = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
with open('day3.txt') as f:
    data = f.read().splitlines()
l = {}
s1 = 0
def checkA(ch,y,x):
    global s1
    n = False
    has = False
    for le in range(1, len(ch)+1):
        x -= le;
        for (dy,dx) in comb:
            if x+dx < 0 or x+dx >= len(data[0]) or y+dy < 0 or y+dy >= len(data):
                continue
            if data[y+dy][x+dx] == '*' and not n:
                l[(y+dy,x+dx)].append(int(ch))
                n = True
            if not (data[y+dy][x+dx].isnumeric() or data[y+dy][x+dx] == '.'):
                has = True
        x += le
    if has:
        s1 += int(ch)
for i,y in enumerate(data):
    for j,x in enumerate(y):
        if x == "*":
            l[(i,j)] = list()
for i,line in enumerate(data):
    a = ""
    for j,o in enumerate(line):
        if o.isnumeric():
            a += str(o)
        else:
            if a == "":
                continue
            else:
                checkA(a,i,j)
                a = ""
    if a != "":
        checkA(a,i,j)
s2 = 0
for el in l.keys():
    if len(l[el]) >= 2:
        s2 += l[el][0] * l[el][1]
print("First star: ", s1)
print("Second star: ", s2)