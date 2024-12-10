lines = []

with open('day3.txt') as f:
    lines = f.readlines()
def firstStar():
    gamma = ''
    epsilion = ''
    for i in range(len(lines[0])-1):
        zero = 0
        one = 0
        for line in lines:
            if(line[i] == '0'): 
                zero+=1
            else: 
                one+=1
        if(zero > one):
            gamma+='0'
            epsilion+='1'
        else:
            gamma+='1'
            epsilion+='0'
    return int(gamma,2)*int(epsilion,2)

def subSecondStar(first,second,lines):
    for i in range(len(lines[0])-1):
        zero = 0
        one = 0
        for line in lines:
            if(line[i] == '0'): 
                zero+=1
            else: 
                one+=1
        if(zero > one):
            for line in lines[:]:
                if(line[i] == first):
                    lines.remove(line)
        else:
            for line in lines[:]:
                if(line[i] == second):
                    lines.remove(line)
        if(len(lines) == 1):
            return int(lines[0],2)
def secondStar():
    return subSecondStar('0','1',lines[:])*subSecondStar('1','0',lines[:])

print(firstStar())
print(secondStar())