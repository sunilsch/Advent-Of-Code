with open('day5.txt') as f:
    ans = 0
    l = []
    for line in f.readlines():
        line = line.strip()
        first = int(line[0:7].replace("B","1").replace("F","0"),2)
        second = int(line[7:10].replace("R","1").replace("L","0"),2)
        id = (first*8)+second
        l.append(id)
        ans = max(ans, id)
    print("First star: ", ans)
    l.sort()
    for i in range(len(l)-1):
        if l[i+1]-l[i] > 1:
            print("Second star: ", l[i]+1)