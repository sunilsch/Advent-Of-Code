from collections import defaultdict
import re
class Node:
    def __init__(self, data):
        self.name = data[0]
        self.flowRate = int(data[1])
        self.neighbors = defaultdict(int)
        for neighbor in data[2:]:
            self.neighbors[neighbor] = 1
    def __repr__(self):
        return f"Node({self.name}, {self.flowRate}, {self.neighbors})\n"
with open('day16.txt') as f:
    nodes = []
    for line in f.readlines():
        nodes.append(Node(re.findall(r"[A-Z][A-Z]|\d+", line)))
for node in nodes:
    for secondNode in nodes:
        if node != secondNode and node.name in secondNode.neighbors:
            curDist = secondNode.neighbors[node.name]
            for neighbor in node.neighbors:
                if neighbor == secondNode.name:
                    continue
                elif neighbor not in secondNode.neighbors:
                    secondNode.neighbors[neighbor] = curDist + node.neighbors[neighbor]
                else:
                    secondNode.neighbors[neighbor] = min(secondNode.neighbors[neighbor], curDist + node.neighbors[neighbor])
            if not node.flowRate:
                del secondNode.neighbors[node.name]
nodeMap = {node.name: node for node in nodes if node.name == 'AA' or node.flowRate}
def solve(currentNode, visited=[], time=0, maxTime=30):
    if time >= maxTime:
        return 0, visited
    node = nodeMap[currentNode]
    score = node.flowRate * (maxTime-time)
    new_visited = visited + [currentNode]
    nextScores = max([solve(neighbor, new_visited, time + node.neighbors[neighbor] + 1, maxTime) for neighbor in node.neighbors if neighbor not in visited])
    return (score + nextScores[0], [currentNode] + nextScores[1])
print("First star: ", solve('AA')[0])
score, path = solve('AA', maxTime=26)
for node in nodeMap.values():
    for p in path[1:]:
        if p in node.neighbors:
            del node.neighbors[p]
secondScore, _ = solve('AA', maxTime=26)
print("Second star: ", secondScore+score)