lines = []
value = 0
newValue = 0
counter = 0
with open('day1.txt') as f:
    for line in f:
        lines.append(line[:-1])
for index, line in enumerate(lines, start=0):
    newValue = value+int(line)
    if(index >= 3):
        newValue -= int(lines[index-3])
        if(newValue > value):
            counter+=1
    value = newValue

print(counter)