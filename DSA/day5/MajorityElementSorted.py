nums = [1, 2, 3, 3, 3, 3, 4]
target = 3

def HashmapMEsorted(nums,target):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    if freq[target] > len(nums) // 2:
        return True
    else:
        return False

def BoyerHEsorted(nums,target):
    candidate=None
    count=0

    for num in nums:
        if count==0:
            candidate=num
        if num==candidate:
            count+=1
        else:
            count-=1
    if candidate==target:
        return True
    else:
        return False

print(HashmapMEsorted(nums,target))