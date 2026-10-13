# CONTAINS DUPLICATE II

# nums = [1,2,3,1]
# k=3
# k=2
nums = [1,1,0,2,3]
k=3

def containsDup2(nums,k):
    hashSet = {}
    for i in range(len(nums)):
        if i > k:
            del hashSet[nums[i-k-1]]
        if nums[i] in hashSet:
            return True

        hashSet[nums[i]] = True

    return False

print(containsDup2(nums,k))
