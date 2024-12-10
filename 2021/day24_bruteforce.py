instructions = []
with open('day24.txt') as f:
    for line in f:
        print(line)
        if line.startswith('inp'):
            i1,i2 = line.strip().split(' ')
            instructions.append([i1,i2])
        else:
            i1,i2,i3 = line.strip().split(' ')
            instructions.append([i1,i2,i3])
print(instructions)
def set(w,x,y,z,new,a):
    if a == 'w':
        return new,x,y,z
    elif a == 'x':
        return w,new,y,z
    elif a == 'y':
        return w,x,new,z
    return w,x,y,new
def MONAD(input):
    i,w,x,y,z = 0,0,0,0,0
    for instruction in instructions:
        i1 = instruction[0]
        i2 = instruction[1]
        if i1 == 'inp':
            w = int(input[i])
            i+=1
        else:   
            i3 = instruction[2]
            if i1 == 'add':
                new = int(eval(i2))+int(eval(i3))
            elif i1 == 'mul':
                new = int(eval(i2))*int(eval(i3))
            elif i1 == 'div':
                new = int(eval(i2))//int(eval(i3))
            elif i1 == 'mod':
                new = int(eval(i2))%int(eval(i3))
            elif i1 == 'eql':
                if int(eval(i2)) == int(eval(i3)):
                    new = 1
                else:
                    new = 0
            else:
                assert False
            w,x,y,z = set(w,x,y,z,new,i2)
    return z
for i in reversed(range(49917929935000)):
    if i % 100  == 1:
        print(i)
    if not '0' in str(i):
        if MONAD(str(i).zfill(14)) == 0:
            print(i)
            break