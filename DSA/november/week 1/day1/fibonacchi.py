class Solution:
    def fib(self, n: int) -> int:
        #Memoization - 48ms
        # def fibMemo(n,cache):
        #     if n<=1:
        #         return n
        #     if n in cache:
        #         return cache[n]
        #     result = fibMemo(n-1,cache)+fibMemo(n-2,cache)
        #     cache[n]=result
        #     return result
        # cache={}
        # return fibMemo(n,cache)

        #without Memoization - 286ms
        if n<=1:
            return n
        return self.fib(n-1)+self.fib(n-2)