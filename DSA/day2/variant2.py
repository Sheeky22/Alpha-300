# Duplicate Zeros

nums = [1,0,2,3,0,4,5,0]

def zeroDup(nums):
    zero=0
    for i in nums:
        if i==0:
            zero+=1
    
    j=len(nums)-1+zero
    i = len(nums)-1

    while i!=j:
        if j<len(nums):
            nums[j]=nums[i]
        j-=1
        if nums[i]==0:
            if j<len(nums):
                nums[j]=nums[i]
            j-=1
        i-=1
    return nums

print(zeroDup(nums))