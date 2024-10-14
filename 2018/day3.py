points = set()
pointsadded = set()
s = 0
data = []
for line in open('day3.txt').read().splitlines():
    ide,d = line.split(" @ ")
    pos,size = d.split(": ")
    x,y = pos.split(",")
    dx,dy = size.split("x")
    data.append((int(x),int(y),int(dx),int(dy),ide))
for x,y,dx,dy,_ in data:
    for i in range(x,x+dx):
        for j in range(y,y+dy):
            if (i,j) in points and (i,j) not in pointsadded:
                s += 1
                pointsadded.add((i,j))
                continue
            points.add((i,j))
print("First star: ", s)
for x,y,dx,dy,ide in data:
    if (all((i,j) not in pointsadded for i in range(x,x+dx) for j in range(y,y+dy))):
        print("Second star: ", ide.replace("#",""))


