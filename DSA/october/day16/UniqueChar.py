class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap={}
        for i in s:
            if i in hashMap:
                hashMap[i]+=1
            else:
                hashMap[i]=1
        for i in range(len(s)):
            if hashMap[s[i]]==1:
                return i
        return -1