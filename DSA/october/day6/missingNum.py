class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        sum=0
        for i in range(len(nums)):
            sum^=nums[i]
            sum^=i+1
        return sum