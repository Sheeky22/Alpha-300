class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        total=0
        for j in nums:
            total+=j
        leftSum = 0

        for i in range(len(nums)):
            rightSum = total - leftSum - nums[i]

            if leftSum == rightSum:
                return i

            leftSum += nums[i]

        return -1