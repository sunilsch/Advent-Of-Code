print("First star: ", sum(((int(x)//3)-2) for x in open('day1.txt').readlines()))
def calc(inp):
    s = 0
    while True:
        inp = (inp//3)-2
        if inp >= 0:
            s += inp
        else:
            break
    return s
print("Second star: ", sum(calc(int(line)) for line in open('day1.txt').readlines()))