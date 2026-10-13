# SINGLE NUMBER

nums = [2,2,1]

def singleNum(nums):
    sum=0
    for i in nums:
        sum^=i
    return sum

print(singleNum(nums))