rules = {}
with open('day14.txt') as f:
    template = f.readline()[:-1]
    for line in f:
        if line != '\n':
            pair, insert = line[:-1].split(' -> ')
            rules[pair] = insert
def oneStar(template):
    for _ in range(10):
        newTemplate = ''
        for i in range(len(template)):
            newTemplate+=template[i]
            if i+1 < len(template):
                newTemplate+=rules[template[i]+template[i+1]]
        template = newTemplate
    character = {}
    for i in template:
        if i in character:
            character[i]+=1
        else:
            character[i]=1
    return max(character.values())-min(character.values())
def twoStars(template):
    counter = {}
    for i in range(len(template)-1):
        if template[i]+template[i+1] in counter:
            counter[template[i]+template[i+1]] += 1
        else:
            counter[template[i]+template[i+1]] = 1
    for _ in range(40):
        newCounter = {}
        for k in counter:
            if k[0]+rules[k] in newCounter:
                newCounter[k[0]+rules[k]] += counter[k]
            else:
                newCounter[k[0]+rules[k]] = counter[k]
            if rules[k]+k[1] in newCounter:
                newCounter[rules[k]+k[1]] += counter[k]
            else:
                newCounter[rules[k]+k[1]] = counter[k]
        counter = newCounter.copy()
    result = {}
    for k in counter:
        if k[0] in result:
            result[k[0]] += counter[k]
        else:
            result[k[0]] = counter[k]
    result[template[-1]] += 1
    return max(result.values())-min(result.values())
print(oneStar(template))
print(twoStars(template))