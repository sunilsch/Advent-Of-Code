rowPoints = set()
row = 2000000 
rowPointsRemove = set()
sensors = []
beacons = []
with open('day15.txt') as f:
    for line in f.readlines():
        # read
        sensor, beacon = line.strip().split(": ")
        sensor = sensor.split(", ")
        sensor[0] = int(sensor[0].split(" ")[2][2:])
        sensor[1] = int(sensor[1][2:])

        beacon = beacon.split(", ")
        beacon[0] = int(beacon[0].split(" ")[4][2:])
        beacon[1] = int(beacon[1][2:])

        # part 1
        d = abs(sensor[1] - beacon[1]) + abs(sensor[0] - beacon[0])
        dy = abs(sensor[1] - row)
        inRow = d*2 - 2*dy
        for i in range(sensor[0]-(inRow//2), sensor[0]+(inRow//2)+1):
            rowPoints.add(i)
        if sensor[1] == row:
            rowPointsRemove.add(sensor[0])
        if beacon[1] == row:
            rowPointsRemove.add(beacon[0])

        # save for part2
        sensors.append(sensor)
        beacons.append(beacon)
# get result from part 1
for x in rowPointsRemove:
    rowPoints.discard(x)
print(len(rowPoints))

def part2(i):
    r = []
    for sensor, beacon in zip(sensors, beacons):
        d = abs(sensor[1] - beacon[1]) + abs(sensor[0] - beacon[0])
        dy = abs(sensor[1] - i)
        inRow = d*2 - 2*dy
        if inRow < 0:
            continue
        first = sensor[0]-(inRow//2)
        second = sensor[0]+(inRow//2)
        r.append((min(first, second), max(first, second)))
    high = 0
    r.sort()
    for i in range(len(r)):
        if r[i][0] > high:
            return r[i][0]-1
        high = max(high, r[i][1])
    return None
for i in range(4000000):
    x = part2(i)
    if x != None:
        print((x*4000000)+i)
        exit()