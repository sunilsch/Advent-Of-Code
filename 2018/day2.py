inp = open('day2.txt').read().splitlines()
print("First star: ", sum(any(x.count(y) == 3 for y in x) for x in inp)*sum(any(x.count(y) == 2 for y in x) for x in inp))
print("Second star: " + next((x[:i] + x[i+1:] for x in inp for y in inp if x != y  for i in range(len(x)) if x[:i] + x[i+1:] == y[:i] + y[i+1:]), None))