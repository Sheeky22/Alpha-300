class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashMap={}
        for i in s:
            if i not in hashMap:
                hashMap[i]=1
            else:
                hashMap[i]+=1
        for i in t:
            if i in hashMap:
                if hashMap[i]==0:
                    return False
                else:
                    hashMap[i]-=1
            else:
                return False
        return True