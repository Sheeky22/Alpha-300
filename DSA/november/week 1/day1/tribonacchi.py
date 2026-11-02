class Solution:
    def tribonacci(self, n: int) -> int:
        def tribMemo(n,cache):
            if n<=1:
                return n
            if n==2:
                return 1
            if n in cache:
                return cache[n]
            result = tribMemo(n-1,cache)+tribMemo(n-2,cache)+tribMemo(n-3,cache)
            cache[n]=result
            return result
        cache={}
        return tribMemo(n,cache)