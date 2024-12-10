instructions = []
coordinatesX = []
coordinatesY = []
with open('day13.txt') as f:
    emptyLine = False
    for line in f:
        if line == '\n':
            emptyLine = True
            continue
        if not emptyLine:
            x,y = line[:-1].split(',')
            coordinatesX.append(int(x))
            coordinatesY.append(int(y))
        else:
            direction, value = line[11:-1].split('=')
            instructions.append([direction,int(value)])
paper = [[False for _ in range(max(coordinatesX)+1)] for _ in range(max(coordinatesY)+1)]
for y,x in zip(coordinatesY,coordinatesX):
    paper[y][x] = True
for c,i in enumerate(instructions):
    if i[0] == 'y':
        newList = paper[:i[1]]
        otherHalf = paper[i[1]+1:]
        for i,x in enumerate(otherHalf):
            for j,y in enumerate(x):
                if y:
                    newList[len(otherHalf)-1-i][j] = True
    else:
        newList = []
        otherHalf = []
        for x in paper:
            oneHalf = []
            secondHalf = []
            for k,y in enumerate(x):
                if k < i[1]:
                    oneHalf.append(y)
                elif k > i[1]:
                    secondHalf.append(y)
            newList.append(oneHalf)
            otherHalf.append(secondHalf)
        for i,x in enumerate(otherHalf):
            for j,y in enumerate(x):
                if y:
                    newList[i][len(otherHalf[0])-1-j] = True
    paper = newList.copy()
    if(c==0):
        cnt = 0
        for x in paper:
            for y in x:
                if y:
                    cnt+=1
        print(cnt)
for x in paper:
    for y in x:
        str = ''
        if y:
            str = '##'
        else:
            str = '  '
        print(str,end=' ')
    print('\n')