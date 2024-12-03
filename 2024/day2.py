s,s2 = 0,0
def check(nums):
    return all(nums[i] > nums[i-1] and abs(nums[i] - nums[i-1])<=3 for i in range(1,len(nums))) or all(nums[i] < nums[i-1] and abs(nums[i] - nums[i-1])<=3 for i in range(1,len(nums)))
for line in open('day2.txt').readlines():
    s2T = False
    nums = [int(y) for y in line.strip().split(" ")]
    for i in range(0, len(nums)):
        nums2 = nums[:i] + nums[1+i:]
        s2T = check(nums2) or s2T
    s += check(nums)
    s2T = check(nums) or s2T
    s2 += s2T
print("First star: ", s)
print("Second star: ", s2)