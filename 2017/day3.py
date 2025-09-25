from collections import defaultdict
n = 312051
def part1():
    layer = 0
    while (2*layer + 1)**2 < n:
        layer += 1
    side_len = 2 * layer
    max_num_in_layer = (2*layer + 1)**2
    steps_from_corner = (max_num_in_layer - n) % side_len
    steps_to_midpoint = abs(steps_from_corner - layer)
    return layer + steps_to_midpoint
def part2():
    grid = defaultdict(int)
    grid[(0, 0)] = 1
    x, y, steps = 0, 0, 1
    while True:
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            for _ in range(steps):
                x += dx
                y += dy
                value = sum(grid[(x + mx, y + my)] for mx in [-1, 0, 1] for my in [-1, 0, 1])
                grid[(x, y)] = value
                if value > n:
                    return value
            if dy != 0:
                steps += 1
print("First star:", part1())
print("Second star:", part2())