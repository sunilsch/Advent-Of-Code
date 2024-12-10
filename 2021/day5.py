area = [[0 for x in range(1000)] for y in range(1000)] 
lines = []
with open('day5.txt') as f:
    for line in f:
        lines.append([int(x) for x in line.replace(" -> ",",").split(",")])
for line in lines:
    if line[0] == line[2]:
        i = line[1]
        if line[1] > line[3]:
            while i >= line[3]:
                area[line[0]][i]+=1
                i-=1
        else:
            while i <= line[3]:
                area[line[0]][i]+=1
                i+=1
    elif line[1] == line[3]:
        i = line[0]
        if line[0] > line[2]:
            while i >= line[2]:
                area[i][line[1]]+=1
                i-=1
        else:
            while i <= line[2]:
                area[i][line[1]]+=1
                i+=1
    else:
        i = line[0]
        j = line[1]
        if line[0] < line[2]:
            while i <= line[2]:
                area[i][j]+=1
                i+=1
                j+=1 if line[1] < line[3] else -1
        else:
            while i >= line[2]:
                area[i][j]+=1
                i-=1
                j-=1 if line[1] > line[3] else -1

counter = 0
for r in area:
    for value in r:
        if value >= 2:
            counter+=1
print(counter)