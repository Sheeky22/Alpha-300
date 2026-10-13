class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]=0
        for i in nums:
            i=abs(i)
            if 1<=i<=len(nums):
                if nums[i-1]>0:
                    nums[i-1]=-nums[i-1]
                elif nums[i-1]==0:
                    nums[i-1]=-1*(len(nums)+1)
        for i in range(1,len(nums)+1):
            if nums[i-1]>=0:
                return i
        return len(nums)+1