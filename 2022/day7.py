from itertools import accumulate
s, r = [], []
for line in open('day7.txt').readlines():
        splitted = line.strip('$').split()
        if splitted == ['cd', '..']:
            r.append(s.pop())
            s[-1] += r[-1]
        elif splitted[0] == 'cd':
            s.append(0)
        elif splitted[0] != 'ls':
            if splitted[0] != 'dir':
                s[-1] += int(splitted[0])
sizes = list(accumulate(s[::-1])) + r 
available = 70000000-max(sizes)
print("First star: ", sum(filter(lambda x: x<=100000, sizes)))
print("Second star: ", min(filter(lambda x: x+available>30000000, sizes)))