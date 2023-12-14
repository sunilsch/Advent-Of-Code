inp = [int(x) for x in open("day1.txt").readline().strip()]
print("First star: ", sum(inp[i] for i in range(len(inp)) if inp[i] == inp[(i+1)%len(inp)]))
print("Second star: ", sum(inp[i] for i in range(len(inp)) if inp[i] == inp[(i+(len(inp)//2))%len(inp)]))