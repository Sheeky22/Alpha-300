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