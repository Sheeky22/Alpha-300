class Solution:
    cache={}

    def fib(self, n: int) -> int:
        def fibMemo(n,cache):
            if n<=1:
                return n
            if n in cache:
                return cache[n]
            result = fibMemo(n-1,cache)+fibMemo(n-2,cache)
            cache[n]=result
            return result
        cache={}
        return fibMemo(n,cache)