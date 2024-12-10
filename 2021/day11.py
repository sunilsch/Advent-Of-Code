octopuses = []
coordinatesX = [0,0,1,-1,1,-1,1,-1]
coordinatesY = [1,-1,0,0,1,1,-1,-1]
flashes = 0
cnt = 0
with open('day11.txt') as f:
    for line in f:
        octopuses.append([int(x) for x in line[:-1]])
def flash(i,j):
    global flashes
    if octopuses[i][j] >= 10:
        flashed[i][j] = True
        octopuses[i][j] = 0
        flashes+=1
        for k,x in enumerate(coordinatesX):
            if (i+x) >= 0 and (i+x) < len(octopuses) and j+coordinatesY[k] >= 0 and j+coordinatesY[k] < len(octopuses[0]):
                octopuses[i+x][j+coordinatesY[k]]+=1
                flash(i+x,j+coordinatesY[k])
while True:
    cnt+=1
    flashed = [[False for _ in range(len(octopuses))] for _ in range(len(octopuses))]
    for i,x in enumerate(octopuses):
        for j,y in enumerate(x):
            x[j]+=1
            flash(i,j)
    for i,x in enumerate(flashed):
        for j,y in enumerate(x):
            if flashed[i][j]:
                octopuses[i][j] = 0
    if cnt == 100:
        print("OneStar: ",flashes)
    if all(all(f) for f in flashed):
        break
print("SecondStar: ",cnt)