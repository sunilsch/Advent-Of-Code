inp = open('day6.txt').read().splitlines()
def generate_next():
    for i in range(len(inp[0])):
        column = [line[i] for line in inp]
        yield max(set(column), key=column.count), min(set(column), key=column.count)
print("First star:", ''.join(c[0] for c in generate_next()))
print("Second star:", ''.join(c[1] for c in generate_next()))