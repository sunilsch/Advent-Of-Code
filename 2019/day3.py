inp = open('day3.txt').read().splitlines()
def lToTuple(li):
    p = {}
    x,y,c=0,0,0
    for ins in li.split(","):
        d = ins[0]
        l = int(ins[1:])
        for _ in range(0,l):
            c += 1
            if d =="U": y-=1
            if d =="R": x+=1
            if d =="D": y+=1
            if d =="L": x-=1
            if (x,y) not in p:
                p[(x,y)] = c
    return p
def distance(p1,p2=(0,0)):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
p1 = lToTuple(inp[0])
p2 = lToTuple(inp[1])
cross = set(p1.keys() & p2.keys())
print("First star: ", min(map(distance, cross)))
print("Second star: ", min(map(lambda p: p1[p]+p2[p], cross)))