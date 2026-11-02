# FIND THE DUPLICATE NUMBER

nums = [1,3,4,2,2]

def dupNum(nums):
    for i in nums:
        i=abs(i)
        if nums[i-1]<0:
            return i
        else:
            nums[i-1]=-nums[i-1]

print(dupNum(nums))