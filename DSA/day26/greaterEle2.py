class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []
        for i in range(2 * n):
            idx = i % n
            while stack and nums[stack[-1]] < nums[idx]:
                prev = stack.pop()
                ans[prev] = nums[idx]
            if i < n:
                stack.append(idx)

        return ans
