from queue import Queue
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
            rules[name].append((rr[0][0], 0, int(rr[0][1]), rr[1]))
        elif rr[0].count(">") == 1:
            rr[0] = rr[0].split('>')
            rules[name].append((rr[0][0], 1, int(rr[0][1]), rr[1]))
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
                if rule[1] == 0:
                    if l[rule[0]] < rule[2]:
                        cur = rule[3]
                        break
                else:
                    if l[rule[0]] > rule[2]:
                        cur = rule[3]
                        break
    if cur == 'A':
        s += sum(l.values())          
print("First star: ", s)
def newRange(l0, rule):
    if rule[1] == 0:   # <
        return (l0[0], min(l0[1], rule[2]-1))
    elif rule[1] == 1: # >
        return (max(l0[0], rule[2]+1), l0[1])
    elif rule[1] == 2: # <=
        return (l0[0], min(l0[1], rule[2]))
    elif rule[1] == 3: # >=
        return (max(l0[0], rule[2]), l0[1])
def getNewL(rule, l):
    if rule[0] == 'x':
        return (newRange(l[0], rule), l[1], l[2], l[3])
    elif rule[0] == 'm':
        return (l[0], newRange(l[1], rule), l[2], l[3])
    elif rule[0] == 'a':
        return (l[0], l[1], newRange(l[2], rule), l[3])
    elif rule[0] == 's':
        return (l[0], l[1], l[2], newRange(l[3], rule))
s2 = 0
q = Queue()
q.put(('in', tuple(tuple([1,4000]) for _ in range(4))))
while not q.empty():
    cur, l = q.get()
    if l[0][0] > l[0][1] or l[1][0] > l[1][1] or l[2][0] > l[2][1] or l[3][0] > l[3][1]: # invalid
        continue
    if cur == 'A': # accepted
        a = (l[0][1] - l[0][0] + 1)*(l[1][1] - l[1][0] + 1)*(l[2][1] - l[2][0] + 1)*(l[3][1] - l[3][0] + 1)
        s2 += a
        continue
    if cur == 'R': # rejected
        continue
    for rule in rules[cur]: # add new rules
        if rule.__class__ == str: # direct rule
            q.put((rule, l))
            break
        newL = getNewL(rule, l) # new range that the rule can be applied to
        q.put((rule[3], newL)) # add new range to queue
        rule = (rule[0], 2 if rule[1] == 1 else 3, rule[2], rule[3]) # edit rule to be the opposite
        l = getNewL(rule, l) # range that doesn't apply to the rule
print("Second star: ", s2)