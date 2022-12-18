runs = 20000
top = 1
top_before = 0
s = []
s2 = []
i = -1
with open('day17.txt') as f:
    moves = [c for c in f.readline().strip()]
rocks = (
    {"points" : ((0,0),(0,1),(0,2),(0,3)), "bottom": 0, "right" : 3},
    {"points" : ((0,1),(1,0),(1,1),(1,2),(2,1)), "bottom": 2, "right" : 2},
    {"points" : ((0,2),(1,2),(2,0),(2,1),(2,2)), "bottom": 2, "right" : 2},
    {"points" : ((0,0),(1,0),(2,0),(3,0)), "bottom": 3, "right" : 0},
    {"points" : ((0,0),(0,1),(1,0),(1,1)), "bottom": 1, "right": 1}
)
field = [['.' for _ in range(7)] for _ in range(4)]
def printField():
    for y in field:
        print("| ",end="")
        for x in y:
            print(x,end="")
        print(" |")
def hasSpaceBottom(rock, x, y):
    for point in rock["points"]:
        yPoint = y + point[0]
        xPoint = x + point[1]
        if yPoint+1 >= len(field):
            return False
        if field[yPoint+1][xPoint] == "#":
            return False
    return True
def hasSpaceLeft(rock, x, y):
    for point in rock["points"]:
        yPoint = y + point[0]
        xPoint = x + point[1]
        if field[yPoint][xPoint-1] == "#":
            return False
    return True
def hasSpaceRight(rock, x, y):
    for point in rock["points"]:
        yPoint = y + point[0]
        xPoint = x + point[1]
        if field[yPoint][xPoint+1] == "#":
            return False
    return True
def push(rock, x,y):
    global i
    i += 1
    if i == len(moves):
        i = 0
    if moves[i] == '<' and x-1 >= 0:
        if not hasSpaceLeft(rock,x,y):
            return x
        x -= 1
    elif moves[i] == '>' and x+rock["right"] < 6:
        if not hasSpaceRight(rock,x,y):
            return x
        x += 1
    return x
maxSu = 0
for runIndex in range(runs):
    top_before = top
    rock = rocks[runIndex % 5]
    while top + 4 + rock["bottom"] < len(field):
        field.remove(['.' for _ in range(7)])
    while top + 4 + rock["bottom"] > len(field):
        field.insert(0, ['.' for _ in range(7)])
    x = 2
    y = 0
    while True:
        x = push(rock,x,y)
        if not hasSpaceBottom(rock,x,y):
            break
        y += 1
    for point in rock["points"]:
        yPoint = y + point[0]
        xPoint = x + point[1]
        assert(field[yPoint][xPoint] == '.')
        field[yPoint][xPoint] = "#"
    top = max(top, len(field)-y)
    s.append(top-top_before)
    s2.append(top)

print("First star: ", s2[2021])


# cycle detection
"""for i in range(1,len(s)-10):
    for j in range(1,10):
        if s[i+j] != s[j]:
            break
    else:
        print(i,s[i],s2[i])"""

first = int((1000000000000-1605) / 1700) * 2654
second = s2[((1000000000000-1605) % 1700)+1605-1]
print("Second star: ", first + second)