# Time Efficient - Recursion with Memoization
class Solution:
    def climbStairs(self, n: int) -> int:
        def climbMemo(n,cache):
            if n==0:
                return 1
            if n==1:
                return 1
            if n in cache:
                return cache[n]
            result = climbMemo(n-1,cache)+climbMemo(n-2,cache)
            cache[n]=result
            return result
        cache={}
        return climbMemo(n,cache)
# Space Efficient -  DP with 2 states
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        prev2 = 1
        prev1 = 1

        for i in range(2, n + 1):
            current = prev2+prev1
            prev2=prev1
            prev1=current

        return prev1