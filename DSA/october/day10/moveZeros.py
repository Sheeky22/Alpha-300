class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=0
        zeros=0
        for i in nums:
            if i!=0:
                nums[k]=i
                k+=1
        for j in range(k,len(nums)):
            nums[j]=0