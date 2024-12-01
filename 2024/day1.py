list1, list2 = zip(*[map(int, x.split()) for x in open('day1.txt').read().splitlines()])
print("First star: ", sum(abs(x[0] - x[1]) for x in zip(sorted(list1),sorted(list2))))
print("Second star: ", sum(a*list2.count(a) for a in list1))