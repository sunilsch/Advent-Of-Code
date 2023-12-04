s = 0
with open('day4.txt') as f:
    lines = f.readlines()
    copies = [1 for _ in range(len(lines))]
    for i,line in enumerate(lines):
        card, winning = line.strip().split(' | ')
        winning = [int(x) for x in winning.strip().split()]
        _, numbers = card.split(': ')
        numbers = [int(x) for x in numbers.strip().split()]
        a = sum(num in winning for num in numbers)
        s += pow(2, a)//2
        for j in range(i+1, i+a+1):
            copies[j] += copies[i]
print("First star: ", s)
print("Second star: ", sum(copies))