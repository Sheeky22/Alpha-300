# SINGLE NUMBER II

nums=[2,2,3,2]

def singleNum2(nums):
    ones=0
    twos=0
    for i in nums:
        ones=(ones^i)&(~twos)
        twos=(twos^i)&(~ones)
    return ones

print(singleNum2(nums))

