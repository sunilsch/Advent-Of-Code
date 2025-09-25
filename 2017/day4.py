words = [line.split() for line in open('day4.txt').read().splitlines()]
print("First star: ", sum(1 for w in words if len(w) == len(set(w))))
print("Second star: ", sum(1 for w in words if len(w) == len(set(tuple(sorted(c)) for c in w))))