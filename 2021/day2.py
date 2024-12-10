def firstStar():
    forward = 0
    height = 0
    with open('day2.txt') as f:
        for line in f:
            current = line.split(" ")
            if(current[0] == "forward"):
                forward+=int(current[1])
            elif(current[0] == "up"):
                height-=int(current[1])
            else:
                height+=int(current[1])
    return forward*height

def secondStar():
    forward = 0
    height = 0
    aim = 0
    with open('day2.txt') as f:
        for line in f:
            current = line.split(" ")
            if(current[0] == "forward"):
                forward+=int(current[1])
                height+=aim*int(current[1])
            elif(current[0] == "up"):
                aim-=int(current[1])
            else:
                aim+=int(current[1])
    return forward*height

print(firstStar())
print(secondStar())