import copy
crates = [
    ["S","C","V","N"],
    ["Z","M","J","H","N","S"],
    ["M","C","T","G","J","N","D"],
    ["T","D","F","J","W","R","M"],
    ["P","F","H"],
    ["C","T","Z","H","J"],
    ["D","P","R","Q","F","S","L","Z"],
    ["C","S","L","H","D","F","P","W"],
    ["D","S","M","P","F","N","G","Z"]
]
crates1 = copy.deepcopy(crates)
crates2 = copy.deepcopy(crates)
with open('day5.txt') as f:
    for line in f.readlines():
        line = line.strip()
        _,amount,_,source,_,dest = line.split(" ")
        amount, source, dest = int(amount), int(source)-1, int(dest)-1
        li = []
        for i in range(amount):
            l = crates1[source].pop() # first
            crates1[dest].append(l) # first
            l = crates2[source].pop() # second
            li.append(l) #second
        li.reverse()
        for l in li:
            crates2[dest].append(l)
print("First star: ", "".join(x[-1] for x in crates1))
print("Second star: ", "".join(x[-1] for x in crates2))