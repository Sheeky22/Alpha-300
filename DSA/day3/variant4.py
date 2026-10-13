# SINGLE NUMBER 3

nums = [1,2,1,3,2,5]

def singleNum3(nums):
    xorr=0
    for i in nums:
        xorr^=i
    rmb=xorr&(-xorr)
    b1=b2=0
    for i in nums:
        if (i&rmb):
            b1^=i
        else:
            b2^=i
    return [b1,b2]

print(singleNum3(nums))