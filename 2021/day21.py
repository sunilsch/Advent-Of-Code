dice = 0
position = [4,8]
score = [0,0]
i = 0
while max(score) < 1000:
    dice+=3
    moves = 3*dice-3
    for j in range(moves):
        position[i] += 1
        if position[i] == 11:
            position[i] = 1
    score[i]+=position[i]
    i = 1 - i
print(min(score)*dice)
DP = {}
position = [10-1,9-1]
def countWins(p1,p2,s1,s2):
    if s1 >= 21:
        return (1,0)
    if s2 >= 21:
        return (0,1)
    if (p1,p2,s1,s2) in DP:
        return DP[(p1,p2,s1,s2)]
    ans = (0,0)
    for d1 in [1,2,3]:
        for d2 in [1,2,3]:
            for d3 in [1,2,3]:
                new_p = (p1+d1+d2+d3)%10
                new_s = s1 + new_p + 1
                x,y = countWins(p2,new_p,s2,new_s)
                ans = (ans[0]+y, ans[1]+x)
    DP[(p1,p2,s1,s2)] = ans
    return ans
print(max(countWins(position[0], position[1], 0, 0)))