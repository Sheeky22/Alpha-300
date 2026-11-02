class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for i in nums:
            a=abs(i)
            if nums[a-1]<0:
                continue
            else:
                nums[a-1]=-nums[a-1]
        res=[]
        for i in range(len(nums)):
            if nums[i]>0:
                res.append(i+1)
        return res

