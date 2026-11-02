arr = [1,2,2,6,6,6,6,7,10]

def hashmapElement25(nums):
    freq={}

    for i in nums:
        freq[i]=freq.get(i,0)+1

    for num,count in freq.items():
        if count>len(nums)//4:
            return num

def boyerElement25(nums):
    candidate=None
    count=0

    for i in nums:
        if candidate!=i:
            candidate=i
            count=1
        else:
            count+=1

        if count>len(nums)//4:
            return i

print(hashmapElement25(arr))
print(boyerElement25(arr))


