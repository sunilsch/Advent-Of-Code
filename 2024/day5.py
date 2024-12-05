from collections import defaultdict
def check(update):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if update[j] not in rules[update[i]]:
                return False
    return True
def newUpdate(update):
    r = defaultdict(set)
    for x in update:
        r[x] = rules[x] & set(update)
    return sorted(r,key=lambda k: len(r[k]), reverse=True)
s1, s2 = 0,0
inp = open('day5.txt').read().split("\n\n")
rules = defaultdict(set)
for x in inp[0].split("\n"):
    a,b = map(int, x.split("|"))
    rules[a].add(b)
updates = [list(map(int, x.split(","))) for x in inp[1].split("\n")]
for update in updates:
    if check(update):
        s1 += update[len(update) // 2]
for update in updates:
    if not check(update):
        new = newUpdate(update)
        s2 += new[len(new) // 2]
print("First star: ", s1)
print("Second star: ", s2)