data = ''
versionSum = 0
with open('day16.txt') as f:
    line = f.readline().strip()
for x in line:
    data+=bin(int(x, 16))[2:].zfill(4)
print(data)
def checkPacket(i):
    global versionSum
    versionSum += int(data[i:i+3], 2)
    typeID = int(data[i+3:i+6], 2)
    if typeID == 4:
        return decodeValue(i+6)
    else:
        return decodeOperator(i+6,typeID)
def decodeValue(i):
    valueStr = ''
    isData = True
    while isData:
        valueStr += data[i+1:i+5]
        if not data[i] == '1':
            isData = False
        i+=5
    value = int(valueStr,2)
    return i,value
def decodeOperator(i,typeID):
    values = []
    lengthID = data[i]
    i=i+1
    if lengthID == '0':
        totalLength = int(data[i:i+15],2)
        i+=15
        j = i
        while i < j+totalLength:
            i,value = checkPacket(i)
            values.append(value)
    else:
        totalNumber = int(data[i:i+11],2)
        i+=11
        for j in range(totalNumber):
            i,value = checkPacket(i)
            values.append(value)
    
    return i,calculateResult(values,typeID)
def calculateResult(values,typeID):
    if typeID == 0:
        return sum(values)
    elif typeID == 1:
        result = 1
        for x in values:
            result*=x
        return result
    elif typeID == 2:
        return min(values)
    elif typeID == 3:
        return max(values)
    elif typeID == 5:
        return values[0] > values[1]
    elif typeID == 6:
        return values[0] < values[1]
    elif typeID == 7:
        return values[0] == values[1]
print('Final value ->',checkPacket(0)[1])
print('Version Sum -> ',versionSum)