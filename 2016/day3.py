triangles = [list(map(int, l.split())) for l in open("day3.txt")]
print("First star:", sum(all(x + y > z for x, y, z in [(a, b, c), (a, c, b), (b, c, a)])
                         for a, b, c in triangles))
print("Second star:", sum(all(x + y > z for x, y, z in [(a, b, c), (a, c, b), (b, c, a)])
                          for i in range(0, len(triangles), 3)
                          for a, b, c in zip(*triangles[i:i+3])))