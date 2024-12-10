import networkx as nx
G = nx.Graph()
visited = {}
with open('day12.txt') as f:
    for line in f:
        x,y = line[:-1].split('-')
        if not x.isupper():
            visited[x] = 0
        G.add_edge(x,y)
nx.draw(G, with_labels=True)
cnt1,cnt2 = 0,0
def run1(node, visited):
    global cnt1
    if node == "end":
        cnt1+=1
        return
    elif node in visited:
        visited[node]+=1
        if visited[node] == 2:
            return
    for i in G.neighbors(node):
        run1(i, visited.copy())
def run2(node, visited):
    global cnt2
    if node == "end":
        cnt2+=1
        return
    elif node in visited:
        c = 0
        visited[node]+=1
        for i in visited:
            if visited[i] > 1:
                c+=1
        if c >= 2 or visited[node] > 2:
            return
        if node == 'start':
            if(visited[node] == 2):
                return
    for i in G.neighbors(node):
        run2(i, visited.copy())
run1('start', visited.copy())
run2('start', visited.copy())
print("1. Stern:", cnt1, "\n2. Stern:", cnt2)