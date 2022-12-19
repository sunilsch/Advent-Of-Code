import math
class BluePrint():
    def __init__(self, blueprintStr):
        id, robots = blueprintStr[10:-1].split(": ")
        self.id = int(id)
        self.robots = {}
        for robot in reversed(robots.split(". ")):
            typ,costs = robot[5:].split(" robot costs ")
            self.robots[typ] = {res : int(n) for n, res in (cost.split(" ") for cost in costs.split(" and "))}
        self.maxRes = {t: max(res.get(t, 0) for res in self.robots.values()) for t in self.robots.keys()}
    def getMaxGeodes(self,min):
        res = {x: 0 for x in self.robots}
        robotsCreated = {t: 1 if t == "ore" else 0 for t in self.robots}
        q = []
        q.append((min,res,robotsCreated,None))
        maxGeodes = 0
        while len(q):
            timeLeft, res, robotsCreated, last = q.pop()
            # time is over
            if timeLeft == 0:
                maxGeodes = max(maxGeodes, res["geode"])
                continue
            # current n of geode will not get bigger than maxGeodes
            if maxGeodes - res["geode"] >= (timeLeft * (2 * robotsCreated["geode"] + timeLeft - 1)) // 2:
                continue
            timeLeft -= 1
            secondAdd = False
            for typ, r in self.robots.items():
                # generated enough
                if typ != "geode" and robotsCreated[typ] * timeLeft + res[typ] > self.maxRes[typ] * timeLeft:
                    continue
                # dont create if we could last time
                if (last is None or last == typ) and all(v <= res[t] - robotsCreated[t] for t, v in r.items()):
                    continue
                # not enough ressources yet, but maybe later
                if any(res[t] < v for t, v in r.items()):
                    secondAdd = secondAdd or all(robotsCreated[t] > 0 for t in r.keys())
                    continue
                newRessource = {t: v + robotsCreated[t] - r.get(t, 0) for t, v in res.items()}
                newRobots = {t: v + (1 if t==typ else 0) for t, v in robotsCreated.items()}
                q.append((timeLeft,newRessource,newRobots,typ))
            if secondAdd:
                newRessource = {t: v + robotsCreated[t] for t, v in res.items()}
                q.append((timeLeft, newRessource, robotsCreated, None))
        return maxGeodes
with open('day19.txt') as f:
    blueprints = [BluePrint(line.strip()) for line in f.readlines()]
print("First star: ", sum(b.id * b.getMaxGeodes(24) for b in blueprints))
print("Second star: ", math.prod(b.getMaxGeodes(32) for b in blueprints[:3]))