class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum=0
        for i in s + t:
            sum^=ord(i)
        return chr(sum)