with open('day6.txt') as f:
    ans = 0
    ans2 = 0
    a = 0
    s = set()
    l = [0 for _ in range(26)]
    lC = 0
    for line in f.readlines():
        if line == "\n":
            ans += a
            a = 0
            s = set()
            for x in l:
                if x == lC:
                    a+=1
            ans2 += a
            a = 0
            lC = 0
            l = [0 for _ in range(26)]
        else:
            line = line.strip()
            lC += 1
            for c in line:
                if not (c in s):
                    s.add(c)
                    a+=1
                l[ord(c)-97]+=1
print("First star: ", ans)
print("Second star: ", ans2)