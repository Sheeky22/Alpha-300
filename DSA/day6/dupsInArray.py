class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        res=[]
        for i in nums:
            i=abs(i)
            if nums[i-1]<0:
                res.append(i)
            else:
                nums[i-1]=-nums[i-1]
        return res