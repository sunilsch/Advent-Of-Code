inp = [y for y in open('day15.txt').read().split(",")]
ans = 0
def calcHash(x):
    h = 0
    for y in x:
        h += ord(y)
        h*=17
        h %= 256
    return h
for x in inp:
    ans += calcHash(x)
print("First star: ", ans)
boxes = [[] for _ in range(256)]
labelToNum = {}
for x in inp:
    if x.endswith("-"):
        label = x[:-1]
        h = calcHash(label)
        if label in boxes[h]:
            boxes[h].remove(label)
    else:
        label = x.split("=")[0]
        num = int(x.split("=")[1])
        h = calcHash(label)
        if label in boxes[h]:
            index = boxes[h].index(label)
            boxes[h][index] = label
            labelToNum[label] = num
        else:
            boxes[h].append(label)
            labelToNum[label] = num
ans2 = 0
for label in labelToNum.keys():
    num = labelToNum[label]
    for i in range(256):
        if len(boxes[i]) >= 1:
            if label in boxes[i]:
                value = i
                index = boxes[i].index(label)
                break
    else:
        continue
    ans2 += num*(value+1)*(index+1)
print("Second star: ", ans2)