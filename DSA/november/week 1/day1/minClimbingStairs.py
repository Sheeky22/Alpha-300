class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        step2=cost[0]
        step1=cost[1]
        n=len(cost)

        for i in range(2,n):
            current=min(step1,step2)
            step2=step1
            step1=current+cost[i]
        return min(step1,step2)