instruction = []
with open('day10.txt') as f:
    for line in f.readlines():
        line = line.strip()
        if line.startswith("n"):
            instruction.append(line)
        else:
            x,y = line.split(" ")
            instruction.append((x,y))
have_something = False
add_save = 0
x = 1
ans = 0
result = []
ind = 0
print("Second star: ")
for i in range(241):
    if i == 40 or i==80 or i==120 or i==160 or i==200 or i==240:
        print("".join(x+" " for x in result))
        result = []
        ind = 0
    if i == 19 or i==59 or i==99 or i==139 or i==179 or i==219:
        ans += (i+1)*x
    if ind >= x-1 and ind <= x+1:
        result.append("#")
    else:
        result.append(" ")
    ind+=1
    if i == 240:
        break
    if not have_something:
        ins = instruction.pop(0)
        if ins != "noop":
            add_save = int(ins[1])
            have_something = True
    else:
        have_something = False
        x += add_save
print("First star: ", ans)