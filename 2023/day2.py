limits = {'red':12, 'green':13, 'blue':14}
s = [0, 0]
with open('day2.txt') as f:
    for line in f.readlines():
        n, maxA = True, {"red":0, "green":0, "blue":0}
        gameID, data = line.strip().split(": ")
        for game in data.strip().split("; "):
            for x in game.split(", "):
                x = x.split(" ")
                if limits[x[1]] < int(x[0]):
                    n = False
                maxA[x[1]] = max(maxA[x[1]], int(x[0]))
        if n:
            s[0] += int(gameID.split(" ")[1])
        s[1] += maxA["red"] * maxA["green"] * maxA["blue"]    
print("First star: ", s[0])
print("Second star: ", s[1])