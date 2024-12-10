patterns = []
values = []
with open('day8.txt') as f:
    for line in f:
        linePattern, lineValue = line.split(' | ')
        patterns.append([x for x in linePattern.split(' ')])
        values.append([y for y in lineValue[:-1].split(' ')])
counter = ['' for _ in range(len(values))]
dict = {2:1,3:7,4:4,7:8}
for i,x in enumerate(values):
    for digit in x:
        if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
            counter[i]+=str((dict[len(digit)]))
        elif len(digit) == 5:
            for y in patterns[i]:
                if len(y) == 2:
                    if y[0] in digit and y[1] in digit:
                        counter[i]+=str(3)
                        break
            else:
                for y in patterns[i]:
                    if len(y) == 4:
                        cnt = 0
                        for k in y:
                            if k in digit:
                                cnt+=1
                        if(cnt == 2):
                            counter[i]+=str(2)
                            break
                        elif(cnt == 3):
                            counter[i]+=str(5)
                            break
        elif len(digit) == 6:
            for y in patterns[i]:
                if len(y) == 4:
                    cnt = 0
                    for k in y:
                        if k in digit:
                            cnt+=1
                    if cnt == 4:
                        counter[i]+=str(9)
                        break
            else:
                for y in patterns[i]:
                    if len(y) == 3:
                        cnt = 0
                        for k in y:
                            if k in digit:
                                cnt+=1
                        if cnt == 3:
                            counter[i]+=str(0)
                            break
                        else:
                            counter[i]+=str(6)
print(sum(int(x) for x in counter))