class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        arr=[0]*len(nums)
        even=0
        odd=1
        for i in nums:
            if i%2==0:
                arr[even]=i
                even+=2
            else:
                arr[odd]=i
                odd+=2
        return arr
