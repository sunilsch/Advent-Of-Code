inp = [int(x) for x in open('day2.txt').readline().split(",")]
def firstStar(li,a,b):
    li[1],li[2] = a,b
    for i in range(0,len(li),4):
        if li[i] == 1:
            li[li[i+3]] = li[li[i+2]] + li[li[i+1]]
        elif li[i] == 2:
            li[li[i+3]] = li[li[i+2]] * li[li[i+1]]
        elif li[i] == 99:
            return li[0]
def secondStar():
    for a in range(0,100):
        for b in range(0,100):
            x = firstStar(list(inp),a,b)
            if x == 19690720:
                return 100*a+b
print("First star: ", firstStar(list(inp),12,2))
print("Second star: ", secondStar())