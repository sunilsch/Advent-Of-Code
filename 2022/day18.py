cubes = set()
with open('day18.txt') as f:
    for line in f.readlines():
        x, y, z = [int(i) for i in line.strip().split(",")]
        cubes.add((x,y,z))
minv = min(min(cube) for cube in cubes) - 1
maxv = max(max(cube) for cube in cubes) + 1
def getNeighbors(cube):
    x, y, z = cube
    neighbors = set()
    if x > minv:
        neighbors.add((x - 1, y, z))
    if x < maxv:
        neighbors.add((x + 1, y, z))
    if y > minv:
        neighbors.add((x, y - 1, z))
    if y < maxv:
        neighbors.add((x, y + 1, z))
    if z > minv:
        neighbors.add((x, y, z - 1))
    if z < maxv:
        neighbors.add((x, y, z + 1))
    return neighbors
area1 = 6 * len(cubes)      
for cube in cubes:
    neighbour = getNeighbors(cube)
    area1 -= len(getNeighbors(cube) & cubes)
print("First star: ", area1)
area2 = 0
points = [(minv, minv, minv)]
s = {points[0]}
while points:
    point = points.pop()
    for neighbour in getNeighbors(point) - s:
        if neighbour in cubes:
            area2 += 1
        else:
            s.add(neighbour)
            points.append(neighbour)
print("Second star: ", area2)