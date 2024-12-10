opened = '([{<'
closed = ')]}>'
points = [3,57,1197,25137]
cnt1 = 0
cnt2List = []
with open('day10.txt') as f:
    for line in f: 
        cnt2 = 0
        openList = []
        line = line.replace('\n','')
        for char in line:
            if char in opened:
                openList.append(char)
            else:
                for i,x in enumerate(closed):
                    if char == x:
                        if not openList[-1] == opened[i]:
                            break
                        else:
                            openList.pop()
                else:
                    continue
                break
        else:
            print(openList)
            for x in reversed(openList):
                for i,y in enumerate(opened):
                    if x == y:
                        cnt2=((5*cnt2)+i+1)
            cnt2List.append(cnt2)
            continue
        cnt1 += points[i]
print(cnt1)
cnt2List.sort()
print(cnt2List[len(cnt2List)//2])