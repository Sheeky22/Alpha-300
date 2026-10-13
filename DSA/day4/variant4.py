# BUILD ARRAY

nums = [0,2,1,5,3,4]

def buildArr(nums):
    for i in range(len(nums)):
            nums[i] += (1024 * (nums[nums[i]] % 1024))
        
    for i in range(len(nums)):
        nums[i] //= 1024
    
    return nums

print(buildArr(nums))