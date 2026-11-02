class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i in range(len(nums)):
            if i > k:
                del seen[nums[i-k-1]]
            if nums[i] in seen:
                return True
            seen[nums[i]] = True
        return False