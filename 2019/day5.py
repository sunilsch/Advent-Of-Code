inp = [int(x) for x in open('day5.txt').readline().split(",")]
def firstStar(li,a):
    i,result = 0,0
    while i < len(li):
        ins = str(li[i])
        opcode = int(ins[-2:])
        modes = [int(x) for x in ins[:-2]]
        if len(modes) == 0:
            modes = [0,0]
        elif len(modes) == 1:
            modes = [0] + modes
        try:
            value1 = (li[li[i+1]] if modes[1] == 0 else li[i+1])
            value2 = (li[li[i+2]] if modes[0] == 0 else li[i+2])
        except: pass
        if opcode == 1:
            li[li[i+3]] = value1 + value2
        elif opcode == 2:
            li[li[i+3]] = value1 * value2
        elif opcode == 3:
            li[li[i+1]] = a
        elif opcode == 4:
            result = value1
        elif opcode == 5:
            i = value2 if not value1 == 0 else i+3
        elif opcode == 6:
            i = value2 if value1 == 0 else i+3
        elif opcode == 7:
            li[li[i+3]] = 1 if value1 < value2 else 0
        elif opcode == 8:
            li[li[i+3]] = 1 if value1 == value2 else 0
        elif opcode == 99:
            return result
        if opcode in [1,2,7,8]:
            i += 4
        if opcode in [3,4]:
            i += 2
print("First star: ", firstStar(list(inp),1))
print("Second star: ", firstStar(list(inp),5))