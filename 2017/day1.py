inp = [int(x) for x in open("day1.txt").readline().strip()]
print(sum(inp[i] for i in range(len(inp)) if inp[i] == inp[(i+(len(inp)//2))%len(inp)]))