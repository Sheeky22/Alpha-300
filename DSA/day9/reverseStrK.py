class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        start = 0
        while start < len(s):
            end = min(len(s) - 1, start + k - 1)
            left, right = start, end
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            start += 2 * k
        return "".join(s)
