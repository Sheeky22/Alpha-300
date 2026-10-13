# FIND ALL DUPLICATES IN AN ARRAY

nums = [4,3,2,7,8,2,3,1]

def dup(nums):
    res=[]
    for i in nums:
        i=abs(i)
        if nums[i-1]<0:
            res.append(i)
        else:
            nums[i-1]=-nums[i-1]
    return res

print(dup(nums))