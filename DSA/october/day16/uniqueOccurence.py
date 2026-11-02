class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        repeat={}
        for i in arr:
            if i in repeat:
                repeat[i]+=1
            else:
                repeat[i]=1
        hashSet={}
        for i in repeat:
            if repeat[i] in hashSet:
                return False
            else:
                hashSet[repeat[i]]=True
        return True