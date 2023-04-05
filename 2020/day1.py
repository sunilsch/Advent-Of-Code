m = {}
values = []
with open('day1.txt') as f:
    for line in f.readlines():
        line = line.strip()
        value = int(line)
        values.append(value)
for i in range(len(values)):
    current = 2020 - values[i]
    for j in range(i+1, len(values)):
        if(m.get(current - values[j]) != None):
            print(values[i]*values[j]*(current-values[j]))
        m[values[j]] = 1