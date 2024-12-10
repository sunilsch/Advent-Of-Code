import ast
numbers = []
with open('day18.txt') as f:
    for line in f:
        numbers.append(ast.literal_eval(line.strip()))
def add(n1,n2):
    if n1 != None:
        n = [n1, n2]
    else:
        n = n2
    return reduce(n)
def reduce(n):
    exploteNotFinished, n1 = explode(n)
    if exploteNotFinished:
        return reduce(n1)
    else:
        splitNotFinished, n2 = split(n)
        if splitNotFinished:
            return reduce(n2)
        else:
            return n2
def split(n):
    if isinstance(n, list):
        splitNotFinshed1, n1 = split(n[0])
        if splitNotFinshed1:
            return True, [n1, n[1]]
        else:
            splitNotFinshed2, n2 = split(n[1])
            return splitNotFinshed2, [n1,n2]
    else:
        if n >= 10:
            return True, [n//2, (n+1)//2]
        else:
            return False,n
def StringToList(n):
    nStr = str(n)
    list = []
    i = 0
    while i < len(nStr):
        if nStr[i] == '[' or nStr[i] == ',' or nStr[i] == ']':
            list.append(nStr[i])
            i += 1
        elif nStr[i] == ' ':
            i += 1
        else:
            j = i
            while j < len(nStr) and nStr[j].isdigit():
                j +=1
            list.append(int(nStr[i:j]))
            i = j
    return list
def explode(n):
    parts = StringToList(n)
    depth = 0
    for i,c in enumerate(parts):
        if c=='[':
            depth+=1 
            if depth == 5:
                left = parts[i+1]
                right = parts[i+3]
                left_i = None
                right_i = None
                for j in range(len(parts)):
                    if isinstance(parts[j],int) and j < i:
                        left_i = j
                    elif isinstance(parts[j],int) and j>i+3 and right_i is None:
                        right_i = j
                if right_i is not None:
                    parts[right_i] += right
                parts = parts[:i] + [0] + parts[i+5:]
                if left_i is not None:
                    parts[left_i] += left
                return True, ast.literal_eval(''.join([str(x) for x in parts]))
        elif c == ']':
            depth -= 1
    return False,n
def magnitude(n):
    if isinstance(n, list):
        return 3*magnitude(n[0]) + 2*magnitude(n[1])
    else:
        return n
def twoStars():
    best = 0
    for x in numbers:
        for y in numbers:
            if x != y:
                result = magnitude(add(x,y))
                best = max(result,best)
    return best
def oneStar():
    result = None
    score = 0
    for x in numbers:
        result = add(result,x)
    score=magnitude(result)
    return score
print(oneStar())
print(twoStars())