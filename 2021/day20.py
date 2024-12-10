image = []
directionsX = [-1,-1,-1,0,0,0,1,1,1]
directionsY = [-1,0,1,-1,0,1,-1,0,1]
with open('day20.txt') as f:
    IEAStr = f.readline().strip()
    f.readline()
    for line in f:
        image.append('.'+line.strip()+'.')
def createInput(list,i):
    strI = ''.join([calculateSign(i) for _ in range(len(list[0]))])
    list.append(strI)
    list.insert(0, strI)
    return list
def calculateSign(i):
    if IEAStr[0] == '#':
        if i%2 == 1:
            return '#'
    return '.'
def calculatePixel(x,y,input,i):
    data = ''
    for xD,yD in zip(directionsX,directionsY):
        if 0 <= (x+xD) < len(input) and 0 <= (y+yD) < len(input[0]):
            if input[x+xD][y+yD] == '#':
                data+='1'
                continue
        else:
            if i%2 == 1:
                data+='1'
                continue
        data+='0'
    return(IEAStr[int(data,2)])
def createOutput(input,i):
    output = ['' for _ in range(len(input))]
    for x in range(len(input)):
        output[x]+=calculateSign(i+1)
        for y in range(len(input[0])):
            output[x] += calculatePixel(x,y,input,i)
        output[x]+=calculateSign(i+1)
    return output
for i in range(50):
    image = createOutput(createInput(image,i),i)
c = 0
for x in image:
    for y in x:
        if y == '#':
            c+=1
print(c)