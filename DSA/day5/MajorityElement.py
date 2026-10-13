# HashMap Approach

nums = [2, 2, 1, 1, 1, 2, 2]


def HashmapME(nums):

    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    for num, count in freq.items():
        if count > len(nums) // 2:
            return num
        break

def BoyerHE(nums):
    candidate=None
    count=0

    for num in nums:
        if count==0:
            candidate=num
        if num==candidate:
            count+=1
        else:
            count-=1
    return candidate

print(BoyerHE(nums))

# print(HashmapME(nums))