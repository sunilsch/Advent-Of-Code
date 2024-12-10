matrix = []
basin = 0
basins = []
field = [[False for _ in range(len(matrix[0]))]for _ in range(len(matrix))]
iList = [1,-1,0,0]
jList = [0,0,1,-1]
with open('day9test.txt') as f:
    for line in f:
        matrix.append([int(x) for x in line[:-1]])
def checkLowPoint(i,j,y):
    try:
        if(y < matrix[i][j]):
            return True
        else:
            return False
    except:
        return True
def calculateBasins(i,j):
    global basin
    if i>=0 and j>=0 and i<len(matrix) and j<len(matrix[0]):
        if matrix[i][j] != 9:
            if not field[i][j]:
                basin+=1
                field[i][j] = True
                for k in range(4):
                    calculateBasins(i+iList[k],j+jList[k])
c = 0
for i,x in enumerate(matrix):
    for j,y in enumerate(x):
        if checkLowPoint(i-1,j,y) and checkLowPoint(i+1,j,y) and checkLowPoint(i,j+1,y) and checkLowPoint(i,j-1,y):
            basin = 1
            field = [[False for _ in range(len(matrix[0]))]for _ in range(len(matrix))]
            field[i][j] = True
            c+=y+1
            for k in range(4):
                    calculateBasins(i+iList[k],j+jList[k])
            basins.append(basin)
print(c)
basins.sort(reverse=True)
print(basins[0]*basins[1]*basins[2])