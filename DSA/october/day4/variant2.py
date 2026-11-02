# RICHEST CUSTOMER WEALTH

nums = [[1,2,3],[3,2,1]]

def maximumWealth(nums):
    rich = 0
    for i in nums:
        rich = max(rich, sum(i))
    return rich

print(maximumWealth(nums))