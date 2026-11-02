# MISSING NUMBER

nums=[3,0,1]

def missingNumber(nums):
    sum=0
    for i in range(len(nums)):
        sum^=nums[i]
        sum^=i+1
    return sum

print(missingNumber(nums))