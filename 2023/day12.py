lines = open("day12.txt").readlines()
save = {}
symbols = ["#", "."]
def getCombinations(chars, nums, curBlockLen, i, j):
    k = (curBlockLen, i, j)
    if k in save:
        return save[k]
    if i == len(chars): # Termination conditions
        if j == len(nums) and curBlockLen == 0: # All blocks are filled (last block not at the end)
            return 1
        elif j == len(nums)-1 and nums[j] == curBlockLen: # All blocks are filled (last block at the end)
            return 1
        else:
            return 0
    s = 0
    for symb in symbols:
        if chars[i] == symb or chars[i] == "?":
            if symb == "." and curBlockLen == 0:
                s += getCombinations(chars, nums, 0, i+1, j) # If we have a dot, we can go on
            elif symb == '.' and curBlockLen > 0 and j < len(nums) and nums[j] == curBlockLen:
                s += getCombinations(chars, nums, 0, i+1, j+1) # If we have a dot and the current block is filled, we can go on
            elif symb == "#":
                s += getCombinations(chars, nums, curBlockLen+1, i+1, j) # If we have a hashtag, we have to increase the current block length and go on
    save[k] = s # Save the result, to make it faster (dynamic programming)
    return s
def solve(part2):
    su = 0
    for line in lines:
        save.clear()
        chars, nums = line.strip().split()
        if part2:
            chars = '?'.join([chars for _ in range(5)])
            nums = ','.join([nums for _ in range(5)])
        nums = [int(x) for x in nums.split(",")]
        s = getCombinations(chars, nums, 0, 0, 0)
        su += s
    return su
print(solve(False))
print(solve(True))