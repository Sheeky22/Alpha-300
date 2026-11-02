# TWO SUM

nums = [2,7,11,15]
target =9

def twoSum(arr,target):
    hashmap={}
    for i in range(len(arr)):
        if (target-arr[i]) in hashmap:
            return [hashmap[target-arr[i]],i]
        else:
            hashmap[arr[i]]=i
    return []

print(twoSum(nums,target))