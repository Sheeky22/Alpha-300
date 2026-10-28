class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strList=s.split()
        lastIndex=len(strList)-1
        return len(strList[lastIndex])