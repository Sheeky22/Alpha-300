class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        decompressedList=[]

        for i in range(0,len(nums),2):
            for j in range(nums[i]):
                decompressedList.append(nums[i+1])
        return decompressedList