d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
with open('day1.txt') as f:
    s = 0
    for line in f.readlines():
        line = line.strip()
        a = ""
        for i,x in enumerate(line):
            if x.isnumeric():
                a += str(x)
                break
            else:
                for y in d:
                    l = len(y)
                    if line[i:i+l] == y:
                        a += str(d[y])
                        break
                else:
                    continue
                break
        for i,x in enumerate(reversed(line)):
            if x.isnumeric():
                a += str(x)
                break
            else:
                for y in d:
                    l = len(y)
                    if line[len(line)-i-l:len(line)-i] == y:
                        print(y)
                        a += str(d[y])
                        break
                else:
                    continue
                break
        s += int(a)
    print(s)