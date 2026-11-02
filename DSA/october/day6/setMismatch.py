class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        N=len(nums)
        x=0 #Duplicate - Missing
        y=0 # D^2 - M^2

        for i in range(N):
            x+=nums[i] - (i+1)
            y+=(nums[i])**2 - (i+1)**2

        missing = (y-x**2)//(2*x)
        duplicate = x+missing

        return [duplicate,missing]
