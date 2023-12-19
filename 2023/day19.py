inp = open('day19.txt').read().split('\n\n')
rul = inp[0].split('\n')
rules = {}
for r in rul:
    r = r.split('{')
    name = r[0]
    rules[name] = []
    r = r[1][:-1].split(',')
    for rr in r:
        if rr.count(':') != 1:
            rules[name].append(rr)
            continue
        rr = rr.split(':')
        if rr[0].count("<") == 1:
            rr[0] = rr[0].split('<')
            rules[name].append((rr[0][0], False, rr[0][1], rr[1]))
        elif rr[0].count(">") == 1:
            rr[0] = rr[0].split('>')
            rules[name].append((rr[0][0], True, rr[0][1], rr[1]))
s = 0
for x in inp[1].split('\n'):
    x = x[1:-1].split(",")
    l = {}
    for y in x:
        l[y[0]] = int(y[2:])
    cur = 'in'
    while cur != 'R' and cur != 'A':
        for rule in rules[cur]:
            if rule.__class__ == str:
                cur = rule
                break
            else:
                if rule[1] == False:
                    if l[rule[0]] < int(rule[2]):
                        cur = rule[3]
                        break
                else:
                    if l[rule[0]] > int(rule[2]):
                        cur = rule[3]
                        break
    if cur == 'A':
        s += sum(l.values())
                    
print(s)