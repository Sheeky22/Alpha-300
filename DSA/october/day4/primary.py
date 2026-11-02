# RUNNING SUM OF 1D ARRAY

nums=[1,2,3,4]

def runningSum(nums):
    sums=nums[0]
    for i in range(1,len(nums)):
        sums+=nums[i]
        nums[i]=sums
    return nums

print(runningSum(nums))